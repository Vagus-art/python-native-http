""" Use the BeautifulSoup and requests Python packages to print out a list 
of all the article titles on the New York Times homepage. """

from bs4 import BeautifulSoup
from requests import get

url = "https://www.nytimes.com/es/"

html = get(url)

soup = BeautifulSoup(html.text,features="html.parser")

titles = soup.find_all('a', attrs={'data-rref': True})

for title in titles:
    print (title.text.strip())
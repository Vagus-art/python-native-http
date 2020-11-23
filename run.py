from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

def rootHandler(base : BaseHTTPRequestHandler):
    base.send_header("Content-type","text")
    base.end_headers
    base.wfile.write("hello!".encode())

def echoHandler(base : BaseHTTPRequestHandler):
    '''
    parses request args and echoes them separated by new lines
    '''
    base.send_header("Content-type","text")
    base.end_headers
    args = [arg for arg in base.path.split("?")[1].split('&')]
    base.wfile.write('\n'.join(args).encode())

def clientHandler(base : BaseHTTPRequestHandler):
    '''
    whatever
    '''
    base.send_header("Content-type","text")
    base.end_headers
    base.wfile.write(base.client_address[0].encode())

routes = [{
    'path': '/',
    'handler': rootHandler
},
{
    'path': '/echo',
    'handler': echoHandler
},
{
    'path': '/client',
    'handler': clientHandler
}
]

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        found = False
        for route in routes:
            if route['path'] == urlparse(self.path).path:
                route['handler'](self)
                found = True
        if found == False:
            self.wfile.write(f"{self.path} not found!".encode())


def main():
    PORT = 3000
    server = HTTPServer(('',PORT),helloHandler)
    print("server running!")
    server.serve_forever()


if __name__ == "__main__":
    main()
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

game_is_on = True

while game_is_on:
    who_won = ''
    print('player 1 plays:')
    player_1 = input()
    print('player 2 plays:')
    player_2 = input()
    if player_1 == 'rock':
        if player_2 == 'scissors':
            who_won = 'player 1'
        elif player_2 == 'paper':
            who_won = 'player 2'
    if player_1 == 'paper':
        if player_2 == 'rock':
            who_won = 'player 1'
        elif player_2 == 'scissors':
            who_won = 'player 2'
    if player_1 == 'scissors':
        if player_2 == 'paper':
            who_won = 'player 1'
        elif player_2 == 'rock':
            who_won = 'player 2'
    print(f"{who_won} won this time")
    print('want to play again?')
    if input() != "yes":
        game_is_on = False

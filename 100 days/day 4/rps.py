import random
print("""WELCOME, LETS PLAY A GAME OF ROCK,PAPER,SCISSORS""")
moves = ['rock','paper','scissors']
computer_moves = random.choice(moves)
flip = True
while flip is not False:
    your_move = input('Enter your move: ').lower()
    if your_move == 'rock' and computer_moves == 'scissors' or your_move == 'paper' and computer_moves== 'rock' or your_move == 'scissors' and computer_moves == 'paper':
        print(f'computer chose {computer_moves} and i chose {your_move} so i win')
    elif your_move == 'scissors' and computer_moves == 'rock' or your_move == 'rock' and computer_moves== 'paper' or your_move == 'paper' and computer_moves == 'scissors':
        print(f' computer chose {computer_moves} and you chose {your_move} so you lose')
    elif your_move == computer_moves or computer_moves == your_move:
        print("it's a draw")
    else:
        print(" enter a valid move ")
    again = input('do you want to go again(Y/N):').upper()
    if again == 'N':
        flip = False


    

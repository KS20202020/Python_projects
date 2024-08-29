import random

def play():
    computer_choice = random.choice(['r', 'p','s'] )
    user_choice = input('(r) for Rock, (p) for Paper, or (s) for Scissors => ').lower()
    
    if computer_choice == user_choice:
        return'the game is tie'
    elif is_win(user_choice, computer_choice):
        return'You win'

    return'you lost'

def is_win(player, computer):
    #returns true if player wins
    #r>s, p>r, s>p
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r')\
        or (player == 's' and computer == 'p'):
        return True
    
print(play())
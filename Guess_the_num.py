import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 to {x}: '))
        if guess < random_number:
            print('Number is small. Try again.')
        elif guess > random_number:
            print('Number is big. Try again.')
    
    print('Congratulation. You did it.')
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #it could be high b\c low = high
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print('Congratulation. The computer guessed correctly.')

computer_guess(1000)
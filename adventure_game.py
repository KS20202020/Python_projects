name = input('Tell me your name: ')

welcome_text = input(f"Welcome {name}. Let's start the game. Do you want to play the game.(y/n)? ").lower()

if welcome_text == 'y':
    answer = input('You are in a hot dessert. You are standing on road. Which way you want to go?(left/right)=> ')
    if (answer.lower() == 'left'):
        left = input('You walk some time. Suddenly you see a truck but it has no fuel. Do you want to use the truck?(y/n)=>')
        if left.lower() == 'y':
            print('You find a gas station. You fueled your truck. At last you will able to go home.')
        else:
            print('You start walking again. You find a gas station. You realize that you made a mistake. At the same time, the heat is increasing and you fell on ground. ')
            print('-----------------GAME OVER------------------')
    else:
        right = input('You walk some time. You find some trees and a pond. You feel very thirsty. Do you want to drink the pond water?(y/n)=> ')
        if right.lower() == 'y':
            print('You drink the pond water. But the water contained some poisionous element. You feel diziy and fell on the ground.')
            print('-----------------GAME OVER------------------')
        else:
            print('You do not drink pond water. But at the same time, the heat is increasing and you fell on ground.')
            print('-----------------GAME OVER------------------')
else:
    quit()
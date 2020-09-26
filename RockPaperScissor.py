# Rock Paper Scissor Game 1.0
# 3-3-2020
# Devoloped by Shahriar Ahmad Fahim Email: shahriarahmadf@gmail.com

import time
from random import choice

Choice = ['rock', 'paper', 'scissor']
try:
    N= int(input('Number of rounds you want to play = '))
except:
    print('Invalid input for number of rounds. Round to be played is considered as 1 autonomously.')
    N=1
if N<1:
    print('Invalid input for number of rounds. Round to be played is considered as 1 autonomously.')
    N=1

print('\n~~~~     USER vs SPECIALIST      ~~~~')
user_score=0
specialist_score=0
user_choice = ''
specialist_choice = ''
time.sleep(0.2)


for i in range(1,N+1):
    print('\n   ROUND '+ str(i))
    print('=======================')
    specialist_choice= choice(Choice)
    user_choice= input('Give your choice (rock/paper/scissor) : ')
    user_choice= user_choice.lower()

    if not user_choice in Choice:
        print('Sorry, invalid input. No point for you this round.')
        print('USER WINS ROUND ' + str(i))

        specialist_score += 1
        print("------------------")
        print('USER SCORE: ' + str(user_score))
        print('SPECIALIST SCORE: ' + str(specialist_score))
        time.sleep(0.2)
        continue

    time.sleep(0.1)
    print('SPECIALIST: '+ specialist_choice)

    time.sleep(0.5)

    if user_choice == specialist_choice:
        print('DRAW')

    elif user_choice == 'rock':
        if specialist_choice == 'scissor':
            user_score += 1
            print('USER WINS ROUND '+str(i))
        else:
            specialist_score += 1
            print('SPECIALIST WINS ROUND ' + str(i))

    elif user_choice == 'paper':
        if specialist_choice == 'rock':
            user_score += 1
            print('USER WINS ROUND ' + str(i))
        else:
            specialist_score += 1
            print('SPECIALIST WINS ROUND ' + str(i))

    else:
        if specialist_choice == 'paper':
            user_score += 1
            print('USER WINS ROUND ' + str(i))

        else:
            specialist_score += 1
            print('SPECIALIST WINS ROUND ' + str(i))

    print("------------------")
    print('USER SCORE: '+ str(user_score))
    print('SPECIALIST SCORE: ' + str(specialist_score))
    time.sleep(0.2)

time.sleep(0.5)
if user_score>specialist_score:
    print('\nUSER WINS THE GAME.')
elif user_score<specialist_score:
    print('\nSPECIALIST WINS THE GAME.')
else:
    print('\nGAME DRAW.')

print('\n©SPECIALIST©')
time.sleep(10)
import random

print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
a:list[int] = [0,1,2]
sam:int = random.choice(a)
computer:int = random.choice(a)
if sam == 0:
    print('You choose: Rock')
    print('Computer choose: Rock')
    print('Its a draw!')
    
if sam == 1:
    print('You choose: Paper')
    print('Computer choose: Paper')
    print('Its a draw!')
if sam == 2:
    print('You choose: Scissor')
    print('Computer choose: Paper')
    print('You win!')

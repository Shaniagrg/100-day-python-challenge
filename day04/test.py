import random

print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
a:list[int] = [0,1,2]
sam:int = random.choice(a)
computer:int = random.choice(a)
if sam == 0 and computer == 0:
           print('You choose: Rock')
           print('Computer choose: Rock')
           print('Its a draw!')
elif sam == 1 and computer == 1:
           print('You choose: Paper')
           print('Computer choose: Paper')
           print('Its a draw!')
elif sam == 2 and computer == 2:
           print('You choose: Scissor')
           print('Computer choose: Scissor')
           print('Its a draw!')
elif sam == 1 and computer == 0:
           print('You choose: Paper')
           print('Computer choose: Rock')
           print('I win')
elif sam == 2 and computer == 0:
           print('You choose: Scissor')
           print('Computer choose: Rock')
           print('You lost')
elif sam == 2 and computer == 1:
           print('You choose: Scissor')
           print('Computer choose: Paper')
           print('I win')

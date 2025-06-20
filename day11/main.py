import random

jack:int = 10
queen:int = 10
king:int = 10
ace:tuple[int,int] = (1,11)

deck_map: dict[str, list[int]] = { 
    'Hearts': [ace, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , jack, queen, king],
    'Diamonds': [ace, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , jack, queen, king],
    'Clubs': [ace, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , jack, queen, king],
    'Spades': [ace, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , jack, queen, king]
}

computer_card:list[int] = [0,0]
my_card:list[int] = [0,0]
for key,value in deck_map.items():
    computer_card = [random.choice(value), random.choice(value)]
    my_card = [random.choice(value), random.choice(value)]
    if computer_card == ace or my_card == ace:
        computer_card = random.choice(ace)
        my_card = random.choice(ace)
print(computer_card)
print(my_card)

#2 card each = random + random 
#Ask continue or end
    #if continue add 1 add a time 
    #end then sum of card and compare
#continue 
#ask split or add
  #if split then it becomes 2 individual 




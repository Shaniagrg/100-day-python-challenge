import random

def winner(computer,user) -> str:
    if computer > user or user > 21 :
        return "You lost"
    elif computer < user or  user < 21:
        return "You Win!!!"

def sum_cards(sum:list[int]) -> int:
    sum = sum[0] + sum[1]
    return sum

def play() -> str:
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
        for i in range(0,2,1):
            if computer_card[i] == ace or my_card[i] == ace:
                computer_card[i] = random.choice(ace)
                my_card[i] = random.choice(ace)
             

    print(f"Your cards: [{my_card}]")
    print(f"The computer's first card: [{computer_card[0]}]")

    continue_game:str = input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_game == "y":
        print("continue game")
    elif continue_game == "n":
        computer_value:int = sum_cards(computer_card)
        my_value:int = sum_cards(my_card)
        print(f"Your hand is: {my_card}, a total of {my_value}.")
        print(f"The computer's hand is {computer_card[0]}, a total of {computer_value} ")
        return winner(computer = computer_value , user = my_value)
    print("Do you want to play again? Type 'y' or 'n': ")

def main() -> None:
    print("Lets play blackjack")
    print (play())
    

if __name__ == '__main__': 
        main()
    

#2 card each = random + random 
#Ask continue or end
    #if continue add 1 add a time 
    #end then sum of card and compare
#continue 
#ask split or add
  #if split then it becomes 2 individual 




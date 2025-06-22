import random
def sum_cards(sum:list[int]) -> int:
    '''
    - sum the cards 

    parameters:
        - sum:list[int]
    return:
        - int
    
    '''
    sum_cards_value:int = 0
    for i in range(0,len(sum),1):
        sum_cards_value = sum_cards_value + sum[i]
    return sum_cards_value


def convert_value(convert:list[str]) -> list[int]:
    '''
    - convert the jack,queen and king to "10" and ace to "11"
    - then type converion from list[string] to list[int]

    parameters:
        - convert:list[str]

    return:
        - list[int]
    '''

    for i in range(0,len(convert),1):
        if convert[i] == "jack" or convert[i] == "queen" or convert[i] == "king":
            convert[i] = "10"
        elif convert[i] == "ace":
            convert[i] = "11"
            
            #if int(dealer[i]) >= 10:
            #elif int(dealer[i]) < 11:
                #dealer[i] == "1"
    for ind in range(0,len(convert),1):
        convert[ind] = int(convert[ind])
    return convert

def check_21(user:list[str],dealer:list[str]) -> str:
    '''
    - call function convert the value for jack,queen,ace and king
    - call function to sum the card to check if its over 21 or not

    parameter:
        - user:list[str]
        - dealer:list[str]
    
    return:
        - string

    '''
    dealer_convert_to_int:list[int] = convert_value(convert=dealer)
    user_convert_to_int:list[int] = convert_value(convert=user)

    user_total:int = sum_cards(sum=user_convert_to_int)
    dealer_total:int = sum_cards(sum=dealer_convert_to_int)

    if user_total > 21:
        return "You lost"
    elif dealer_total > 21:
        return "You Win!!!"
    
def play(deck_map:dict[str, list[str]],pairs_of_cards:list[list[str]]) -> None:

    '''
    - ramdomly choose 2 values out from the 4 ramdom kayes for both computer and user
    - then create a variable to store used_cards to avoid repetition
    - call funtion to continue/split/end game

    parameters
        - deck_map
        - pairs_of_cards

    return
        -  None
    '''
    used_cards:list[list[str]]= []
    computer_card:dict[str, list[str]] = {"hand1": []}
    my_card:dict[str, list[str]] = {"hand1": []}

    for i in range (0,2,1):

        while True:
            random_key:str = random.choice(list(deck_map.keys()))
            random_value:str = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                my_card["hand1"].append(random_value)
                break
            
        while True:
            random_key:str = random.choice(list(deck_map.keys()))
            random_value:str = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                computer_card["hand1"].append(random_value)
                break

    print(f"Your cards: {my_card}")
    print(f"The computer's first card: {computer_card['hand1'][0]}")
    initial_21_check:str = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])
    if initial_21_check == "You lost":
        print("You lost the game")
    elif initial_21_check == "You Win!!!":
        print("You won the game")
    else:
        print("continue")


def main() -> None:
    '''
    Create a map for all the cards 
    Also create pairs for split

    parameters:
        - None
    
    return:
        None
    '''
    print("Lets play blackjack")
    deck: dict[str, list[str]] = { 
        'Hearts': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Diamonds': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Clubs': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Spades': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    }
    pairs:list[list[str]] = [
        ["ace", "ace"],
        ["jack", "jack"],
        ["2", "2"],
        ["3", "3"],
        ["4", "4"],
        ["5", "5"],
        ["6", "6"],
        ["7", "7"],
        ["8", "8"],
        ["9", "9"],
        ["10", "10"],
        ["queen", "queen"],
        ["king", "king"]
    ]
    print (play(deck,pairs))
    

if __name__ == '__main__': 
        main()
    

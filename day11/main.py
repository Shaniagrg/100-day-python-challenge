import random

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
    computer_card:dict[str, list[str]] = {"cards": []}
    my_card:dict[str, list[str]] = {"cards": []}

    for i in range (0,2,1):

        while True:
            random_key = random.choice(list(deck_map.keys()))
            random_value = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                my_card["cards"].append(random_value)
                break
            
        while True:
            random_key = random.choice(list(deck_map.keys()))
            random_value = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                computer_card["cards"].append(random_value)
                break

    print(f"Your cards: {my_card}")
    print(f"The computer's first card: {computer_card['cards'][0]}")
    print(used_cards)
    print(my_card)
    print(computer_card)


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
    

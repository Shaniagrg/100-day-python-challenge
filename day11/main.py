import random

def play():
    deck_map: dict[str, list[str]] = { 
        'Hearts': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Diamonds': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Clubs': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Spades': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    }

    used_cards:list[list[str]] = []
    computer_card:list[str] = []
    my_card:list[str] = []

    for i in range (0,2,1):

        while True:
            random_key = random.choice(list(deck_map.keys()))
            random_value = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                my_card.append(random_value)
                break
            
        while True:
            random_key = random.choice(list(deck_map.keys()))
            random_value = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                computer_card.append(random_value)
                break
def main() -> None:
    print("Lets play blackjack")
    print (play())
    

if __name__ == '__main__': 
        main()
    

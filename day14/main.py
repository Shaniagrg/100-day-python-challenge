import random

def compare(a:list[str],b:list[str]) -> list[int]:
    player_A:int = int(a[0])
    player_B:int = int(b[0])
    players_value:list[int] = [player_A,player_B]
    return players_value

def people() -> list[str]:
    
    celebrities:dict[str,list[str]] ={"100": [ "Neymar, a Footballer, from Brasil"], 
                                        "600": ["Ariana Grande, a Musician and actress, from United States"], 
                                        "20": ["Justin Bieber, a Musician, from Canada"],
                                        "55": ["Chiritiano, a footballer, from Spain"],
                                        "86": ["Jeff Bezoz. founder of Amazon, from United States"],
                                        "11": ["Kancha, founder of AI , from Dubai"],
                                        "2": ["Mark, founder of Facebook, from United States"]}
    for key,value in celebrities.items():
        random_key:str = random.choice(list(celebrities.keys())) 
        random_value:str = random.choice(celebrities[random_key])
        random_key_value:list[str] = [random_key,random_value]
        return random_key_value

def play() -> None:
    while True:
        #correct add\n
        random_people_A:list[str] = people()
        compare_a = print(f"Compare A: {random_people_A[1]} ")

        random_people_B:list[str] = people()
        compare_b = print(f"Compare B: {random_people_B[1]}")
        user_input:str = input("Who do you think has more followers? Type'a', or 'b': ")
        compare_number: list[int] = compare(a = random_people_A, b =random_people_B)
        #print(compare_number)

        #incorrect you score is 
        continue_game:str = input("Do you want to play again? Type 'y' or 'n': ")
        if continue_game == 'y':
            continue
        elif continue_game == 'n':
            print("Thanks for playing")
            break
        else:
            print("type the correct word")
            continue

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
    
    play()
    

if __name__ == '__main__': 
        main()
    



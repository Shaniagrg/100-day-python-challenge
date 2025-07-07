import random

def compare(a:list[str],b:list[str]) -> str:
    player_A:int = int(a[0])
    player_B:int = int(b[0])

    if player_A > player_B:
        # A is the winner
        return "a"
    elif player_A < player_B:
        #B is the winner
        return "b"
    
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
    correct:int = 0 
    while True:

        while True:
            random_people_A:list[str] = people()
            random_people_B:list[str] = people()
            if random_people_A == random_people_B:
                continue
            else:
                break

        compare_a = print(f"Compare A: {random_people_A[1]} ")
        compare_b = print(f"Compare B: {random_people_B[1]}")
        compare_number: str = compare(a = random_people_A, b =random_people_B)
        user_input:str = input("Who do you think has more followers? Type'a', or 'b': ")
        if compare_number == "a" and user_input == "a":
            correct = correct + 1
            print(f"correct your current score is {correct} ")

        elif compare_number == "b" and user_input == "b":
            correct = correct + 1
            print(f"correct your current score is {correct}")


        else:
            if correct == 0 or correct == 1:
                if correct == 1:
                    correct = correct - 1
                    print(f"incorrect your current score is {correct}")
                else:
                    print(f"incorrect your current score is {correct}")

                continue_game:str = input("Do you want to play again? Type 'y' or 'n': ")
                if continue_game == 'y':
                    continue
                elif continue_game == 'n':
                    print("Thanks for playing")
                    break
                else:
                    print("type the correct word")
                    continue
            else:
                correct = correct - 1
                print(f"incorrect your current score is {correct}") 


        

def main() -> None:
    print("Lets play")
    
    play()
    

if __name__ == '__main__': 
        main()
    



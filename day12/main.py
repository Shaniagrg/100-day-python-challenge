import random 
def user_guessing(guess_number: int) -> None:

    '''
    user get 5 tries 
    append th gussed letter to avoid repeatition 
    
    parameter:
        - guess_number: int

    return:
        - None
    '''
    tries:int = 5 
    guessed_number: list[int] = []

    while True:
        user_guess:int = int(input("Take a guess: "))
        if user_guess in guessed_number:
            print(f"Already used number. Try another.")
            continue
        elif user_guess not in guessed_number:
            if user_guess == guess_number:
                print(f"Correct! The answer was {guess_number} . Thanks for completing that!")
                break 
            else:
                tries = tries - 1
                print(f"You have {tries} guesses left for the number that I'm thinking of.")
                if tries == 0:
                    print(f"Game over. The word was '{guess_number}.'")
                    break 
                else:
                    guessed_number.append(user_guess)
    return            

def get_random_value() -> int:
    '''
    get random value for the container

    parameter:
        - None
    
    return:
        - str
    '''
    number_range:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    random_choose:int = random.choice(number_range)
    return random_choose
     
def play() -> None:
    
    
    while True:
        guess_number: int = get_random_value()

        print("Welcome to Guess The number")

        print("I'm thinking of a number between 1 to 100, try to guess it.")
        game_level:str = input("Choose a difficulty. Type 'easy' or 'hard': ")
       
        user_guessing(guess_number)
             
        #print("too high or too low")
    
        continue_game:str = input("Do you want to play again? Type 'y' if yes and 'n' to quit:  ")
        if continue_game == 'y':
            continue
        if continue_game == 'n':
            print("goodbye")
            return


def main() -> None:
    play()
    

if __name__ == '__main__': 
        main()
    
#Computer has a number in its head form range 1 - 100
#player guess the number
#player can choose the level hard/easy/intermediate
#the guessed number could be high or low
#player has 5 tries to guess the number correctly
#after the tries gone the user loose 
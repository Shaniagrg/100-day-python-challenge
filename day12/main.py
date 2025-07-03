import random 

def pointer_for_guess(user_number_guess:int ,answer:int, p1:int, p2:int) -> list[int]:
    '''
    decrement the value if the user guess is too high 
    increment the value if the user guess is too low

    paramenter:
        - user_number_guess:int 
        - answer:int
        - p1:int
        - p2:int

    return:
        - list[int]
    '''
    if user_number_guess > answer:
        p2 = user_number_guess - 1
        print(f"Too high. Your range is {p1} to {p2}")
    elif user_number_guess < answer:
        p1 = user_number_guess + 1
        print(f"Too low. Your range is {p1} to {p2}")
    guess_range:list[int] = [p1,p2]
    return guess_range

def user_guessing_easy(computer_number: int) -> None:

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
    pointer_beginning:int = 1
    pointer_end:int = 21

    while True:
        user_guess:int = int(input("Take a guess: "))
        if user_guess in guessed_number:
            print(f"Already used number. Try another.")
            continue
        elif user_guess not in guessed_number:
            if user_guess == computer_number:
                print(f"Correct! The answer was {computer_number} . Thanks for completing that!")
                break 
            else:
                tries = tries - 1
                print(f"You have {tries} guesses left for the number that I'm thinking of.")
                user_guess_range:int = pointer_for_guess(user_number_guess = user_guess  , answer=computer_number, p1=pointer_beginning, p2=pointer_end)
                pointer_beginning = user_guess_range[0]
                pointer_end = user_guess_range[1]
                
                if tries == 0:
                    print(f"Game over. The word was '{computer_number}.'")
                    break 
                else:
                    guessed_number.append(user_guess)
    return            


def user_guessing_hard(computer_number: int) -> None:

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
    pointer_beginning:int = 1
    pointer_end:int = 100

    while True:
        user_guess:int = int(input("Take a guess: "))
        if user_guess in guessed_number:
            print(f"Already used number. Try another.")
            continue
        elif user_guess not in guessed_number:
            if user_guess == computer_number:
                print(f"Correct! The answer was {computer_number} . Thanks for completing that!")
                break 
            else:
                tries = tries - 1
                print(f"You have {tries} guesses left for the number that I'm thinking of.")
                user_guess_range:int = pointer_for_guess(user_number_guess = user_guess  , answer=computer_number, p1=pointer_beginning, p2=pointer_end)
                pointer_beginning = user_guess_range[0]
                pointer_end = user_guess_range[1]
                
                if tries == 0:
                    print(f"Game over. The word was '{computer_number}.'")
                    break 
                else:
                    guessed_number.append(user_guess)
    return            

def get_random_value() -> int:
    '''
    get random value for random randrange

    parameter:
        - None
    
    return:
        - str
    '''

    random_choose:int = random.randrange(1, 101)  #will give me ramdom number from 1 to 100
    return random_choose
     
def play() -> None:
    
    
    while True:
        guess_number: int = get_random_value()

        print("Welcome to Guess The number")

        print("I'm thinking of a number between 1 to 100, try to guess it.")
        while True:

            game_level:str = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if game_level == 'hard':
                user_guessing_hard(guess_number)
                break
            elif game_level == 'easy':
                user_guessing_easy(guess_number)
                break
            else:
                print("Type the correct word")
                continue
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
import random 

def pointer_for_guess(user_number_guess:int ,answer:int, pointers_check=list[int]) -> None:
    '''
    decrement the value if the user guess is too high 
    increment the value if the user guess is too low

    paramenter:
        - user_number_guess:int 
        - answer:int
        - pointers_check=list[int]

    return:
        - None
    '''
    #guess_range:list[int] = [p1,p2]
    if user_number_guess > answer:
        pointers_check[1] = user_number_guess - 1
        print(f"Too high. Your range is {pointers_check[0]} to {pointers_check[1]}")
    elif user_number_guess < answer:
        pointers_check[0] = user_number_guess + 1
        print(f"Too low. Your range is {pointers_check[0]} to {pointers_check[1]}")
    return 


def user_guessing(computer_number: int,pointers:list[int]) -> None:

    '''
    user get 5 tries 
    append th gussed letter to avoid repeatition 
    
    parameter:
        - guess_number: int
        - pointers:list[int]

    return:
        - None
    '''
    tries:int = 5 
    guessed_number: list[int] = []

    while True:
        user_guess:int = int(input("Take a guess: "))
        
        if user_guess in guessed_number:
            for i in range(0,len(guessed_number),1):
                if user_guess == guessed_number[i]:
                    print(f"Already used number. Try another.")
            continue
        elif user_guess not in guessed_number:
            if user_guess == computer_number:
                print(f"Correct! The answer was {computer_number} . Thanks for completing that!")
                break 
            else:
                tries = tries - 1
                print(f"You have {tries} guesses left for the number that I'm thinking of.")
                pointer_for_guess(user_number_guess = user_guess  , answer=computer_number, pointers_check = pointers)
                
                if tries == 0:
                    print(f"Game over. The answer was '{computer_number}.'")
                    break 
                else:
                    guessed_number.append(user_guess)
                    continue
    return            

def get_random_value(level:str) -> int:
    '''
    get random value for random randrange

    parameter:
        - level:str
    return:
        - int
    '''
    random_choose:int = 0
    if level == 'easy':
        random_choose = random.randrange(1, 21)  #will give me ramdom number from 1 to 21
    elif level == 'hard':
        random_choose = random.randrange(1, 101)  #will give me ramdom number from 1 to 100
    return random_choose
     
def play() -> None:
    
    
    while True:
        
        guess_number: int = 0

        print("Welcome to Guess The number")

        while True:
            game_level:str = input("Choose a difficulty. Type 'easy' or 'hard': ")
            if game_level == 'hard':
                print("I'm thinking of a number between 1 to 100, try to guess it.")
                pointers_hard:list[int] = [1,100]
                guess_number = get_random_value(level=game_level)
                user_guessing(guess_number,pointers = pointers_hard)
                break
            elif game_level == 'easy':
                print("I'm thinking of a number between 1 to 20, try to guess it.")
                pointers_easy:list[int] = [1,21]
                guess_number = get_random_value(level=game_level)
                user_guessing(guess_number, pointers = pointers_easy)
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
    
#Computer has a number in its head from range 1 - 100
#player guess the number
#player can choose the level hard/easy/intermediate
#the guessed number could be high or low
#player has 5 tries to guess the number correctly
#after the tries gone the user loose 
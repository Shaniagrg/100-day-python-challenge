import random 
def get_random_value() -> int:
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
    
    tries:int = 5 
    
    while True:
        guess_number: int = get_random_value()

        print("Welcome to Guess The number")

        print("I'm thinking of a number between 1 to 100, try to guess it.")
        game_level:str = input("Choose a difficulty. Type 'easy' or 'hard': ")

        print("You have 5 guesses left for the number that I'm thinking of.")
        user_guess:str = input("Tale you guess: ")
        print("too high or too low")
        
        print("You have 4 guesses left for the number that I'm thinking of.")
        print("Correct! The answer was 45. Thanks for completing that!")
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
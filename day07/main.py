#Steps: 
# 1: Display word -> array[str]
# 2: Guess letter -> input()
# 3: check -> if conditionals with 1
# 4: tries 5 -> loop decrement 
#5 tries and 1 word at a time

answer:str = "redadge"
x:list[str] = ["_","_","_","_","_","_","_",]
guessed_letters:set[str] = set()

lives:int = 3

while True:
    guess:str = input("Guess the letter: ")
    if guess in guessed_letters:
        print("Already used. Try another letter.")
    elif guess in answer:
        for ind in range(0,len(answer),1):
            if guess == answer[ind]:
                x[ind] = answer[ind] 
        if ''.join(x) == answer:   # ''.join(variable) concats string from lists 
            print(x)
            print("You won the game!!")
            break
    elif guess not in answer:
        lives = lives - 1
        print(f"{guess} is not the letter. You have {lives} life remain.")
        if lives == 0:
            print(f"Game over. The word was '{answer}.'")
            break
      
    guessed_letters.add(guess)
    print(x)


#Duplicate 
#right 
#wrong looses tires 
#Steps: 
# 1: Display word -> array[str]
# 2: Guess letter -> input()
# 3: check -> if conditionals with 1
# 4: tries 5 -> loop decrement 
#5 tries and 1 word at a time

answer:str = "redadge"
x:list[int] = ["_","_","_","_","_","_","_",]
guessed_letters:set[str] = set()

i:int = 0
while (i < 3):
    i = i + 1
    guess:str = input("Guess the letter: ")
    final:str = ""
    
    if guess in answer and guess not in guessed_letters:
        i = i -1 
        for ind in range(0,len(answer),1):
            if guess == answer[ind]:
                x[ind] = answer[ind]
        for index in range(0,len(x),1):
            final = final + x[index]
        if final == answer:
            print(x)
            print("You have won the game!")
            break   
    elif guess in answer and guess in guessed_letters: 
        print("Already used. Try another letter.")
        i = i -1
    elif guess not in answer and guess in guessed_letters:
        print("Already used. Try another letter.")
        i = i -1
    elif guess not in answer and guess not in guessed_letters:
        print(f"{guess} is not the letter. You have lost 1 life.")
    if i == 3:
        print("Game over")
        print(f"The word was '{answer}'.")
    guessed_letters.add(guess)
    print(guessed_letters)
    print(x)

#if guess in answer and guess NOT in guessed_letters:  add the letter
#if guess in answer and guess in guessed_letters:  used letter try agian
#if guess NOT in answer and guess NOT in guessed_letters:  LOOSE TRY
#if guess NOT in answer and guess in guessed_letters: used letter try again
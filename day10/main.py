def play() -> None:
    
    while True:
        first_number:float = float(input("What is the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
        math_operation:str = input("Type a math operation: ")
        next_number:float = float(input("What is the next number?: "))
        final_answer:float = 0.0
        

        if math_operation == "+":
            final_answer = first_number + next_number
        elif math_operation == "*":
            final_answer = first_number * next_number
        elif math_operation == "/":
            final_answer = first_number / next_number
        elif math_operation == "-":
            final_answer = first_number - next_number
        print(final_answer)

def main() -> None:
        play()
    
if __name__ == '__main__': 
    main()
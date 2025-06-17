def continue_calculating(user_output:float) -> str:
    '''
    ask user if they want to continue the game or not
    call the function input_number if typed "y"
    
    parameters: 
        - user_output:float
    
    returns string
    '''
    while True:
        print(f"Type 'y' to continue calculating with {user_output}, type 'n' to exit or type 'new' for a brand new calculation")
        proceed_calculation:str = input("Type y/n/new: ") 
        if proceed_calculation == 'y':
            user_output = input_number(first_number=user_output)
            continue
        elif proceed_calculation == 'n':
            return "goodbye"
        elif proceed_calculation == 'new':
            return "new"

def operator(user_operation:str,value1:float,value2:float) -> float:

    '''
    check which operator it matches with and calculate
    
    parameters: 
        - user_operation:str
        - value1:float 
        - value2:float

    returns float
    '''

    if user_operation == "+":
        final_answer:float = value1 + value2
    elif user_operation == "*":
        final_answer:float = value1 * value2
    elif user_operation == "/":
        final_answer:float = value1 / value2
    elif user_operation == "-":
        final_answer:float = value1 - value2
    return final_answer



def input_number(first_number:float) -> float:

    '''
    Pass the number for calculation
    Then based on operator calculate to get the value
    
    parameters: 
        - first_number:float

    returns float
    '''

    #first_number:float = float(input("What is the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    math_operation:str = input("Type a math operation: ")
    next_number:float = float(input("What is the next number?: "))
    return operator(user_operation=math_operation,value1=first_number,value2=next_number)
     
def play() -> None:
    
    while True:
        first_number:float = float(input("What is the first number?: "))
        user_output:float = input_number(first_number)

        resume:str = continue_calculating(user_output)
        if resume == "new":
            continue
        elif resume == "goodbye":
            print("Goodbye")
            break

def main() -> None:
        play()
    
if __name__ == '__main__': 
    main()
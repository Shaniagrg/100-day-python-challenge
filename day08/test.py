
def funct_input(convert_message:str, letters_index:str) -> str:

    print("Type your message:")
    message:str = input("")
    print("Type the shift number:")
    shift_number:int = int(input(""))
    secret_message:str = ""

    for ind in range(0,len(message),1):
        current_letter:str = message[ind]
        for i in range(0,len(letters_index),1):
            if current_letter == letters_index[i]:  
                if convert_message == "encode":
                    secret:int = (i + shift_number) % 26   
                    secret_message = secret_message + letters_index[secret]
                elif convert_message == "decode":
                    secret: int = (i - shift_number) % 26  # minus - shift backward
                    secret_message = secret_message + letters_index[secret] 
    
    #print(f"Here's the result: {secret_message}.")
    return secret_message 

def description() -> None:

    while True:

        letters:list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        type_word:str = input("")   

        print(f"Here's the result: {funct_input(type_word,letters)}")

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break

description()
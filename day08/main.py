

def change_message(letters_index:list[str],convert_message_to:str,shift_number:str,message:str) -> str:
    '''
    first transfer the message and list of letters
    Then convert the message

    parameters:
        - letters_index: list[str]
        - convert_message_to: str
        - shift_number: str
        - message: str

    returns: str
    '''
    secret_message:str = ""
    for ind in range(0,len(message),1):
        current_letter:str = message[ind]
        for i in range(0,len(letters_index),1):
            if current_letter == letters_index[i]:  
                if convert_message_to == "encode":
                    secret:int = (i + int(shift_number)) % 26   
                    secret_message = secret_message + letters_index[secret]
                elif convert_message_to == "decode":
                    secret: int = (i - int(shift_number)) % 26  # minus - shift backward
                    secret_message = secret_message + letters_index[secret] 
    return secret_message

    
#print(f"Here's the result: {secret_message}.")
    
def create_message(convert_message_to:str, letters_index:list[str]) -> str:
    '''
    Create message and the computer will encrypt/decrypt for you
    
    parameters: 
        - convert_message_to:str
        - letters_index:list[str]
    
    returns string
    '''
    print("Type your message:")
    message:str = input("")
    print("Type the shift number:")
    shift_number:int = input("")
    #return secret_message 
    return change_message(letters_index,convert_message_to,shift_number,message)

def play() -> None:

    '''
    Type if you want to encrypt or decrypt.

    parameters: None
    
    returns:None
    '''
    while True:

        letters:list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        type_word:str = input("")   

        print(f"Here's the result: {create_message(type_word,letters)}")

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break

def main() -> None:
    play()
    
if __name__ == '__main__': 
    main()
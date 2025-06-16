def convert_message_to_decode(letters_index:list[str],secret_message:str,secret:int) -> str:
    '''
    Decode the message by concating the string to form a word 

    parameters:
        - letters_index: list[str]
        - secret_message:str
        - secret:int

    returns: str
    '''
    secret_message = secret_message + letters_index[secret] 
    return secret_message

def convert_message_to_encode(letters_index:list[str],secret_message:str,secret:int) -> str:
    '''
    Encode the message by concating the string to form a word 

    parameters:
        - letters_index: list[str]
        - secret_message:str
        - secret:int

    returns: str
    '''
    secret_message = secret_message + letters_index[secret]
    return secret_message

def letter_position(letters_index:list[str],convert_message_to:str,shift_number:int,secret_message:str,current_letter:str) -> str:
    '''
    Position the letter serially and change based on shift number

    parameters:
        - letters_index: list[str]
        - current_letter:str
        - convert_message_to:str
        - secret_message:str
        - shift_number:int

    returns: str
    '''
    for i in range(0,len(letters_index),1):
        if current_letter == letters_index[i]:  
            if convert_message_to == "encode":
                secret:int = (i + int(shift_number)) % 26   
                return convert_message_to_encode(letters_index,secret_message,secret)
                
            elif convert_message_to == "decode":
                secret: int = (i - int(shift_number)) % 26  # minus - shift backward
                return convert_message_to_decode(letters_index,secret_message,secret)
                  
    
def create_message(convert_message_to:str, letters_index:list[str]) -> None:
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
    secret_message:str = ""
    for ind in range(0,len(message),1):
        current_letter:str = message[ind]
    print(f"Here's the result: '{letter_position(letters_index,convert_message_to,shift_number,secret_message,current_letter)}'.")
    return None

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

        create_message(convert_message_to=type_word,letters_index=letters)

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break

def main() -> None:
    play()
    
if __name__ == '__main__': 
    main()
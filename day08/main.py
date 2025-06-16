
def convert_message_to_decode(letters_index:list[str], i:int, shift_number:int) -> str:
    '''
    Decode the message 

    parameters:
        - letters_index: list[str]
        - i:int
        - shift_number:int


    returns: str
    '''
    secret:int = (i - shift_number) % 26   
    secret_message:str = letters_index[secret]
    return secret_message

def convert_message_to_encode(letters_index:list[str], i:int, shift_number:int) -> str:
    '''
    Encode the message  

    parameters:
        - letters_index: list[str]
        - i:int
        - shift_number:int

    returns: str
    '''
    secret:int = (i + shift_number) % 26   
    secret_message:str = letters_index[secret]
    return secret_message

def letter_position(letters_index:list[str] , convert_message_to:str , shift_number:int , current_letter:str) -> str:
    '''
    Position the letter serially and change based on shift number

    parameters:
        - letters_index: list[str]
        - convert_message_to:str
        - shift_number:int
        - current_letter:str

    returns: str
    '''
    for i in range(0,len(letters_index),1):
        if current_letter == letters_index[i]:  
            if convert_message_to == "encode":   
                return convert_message_to_encode(letters_index, i ,shift_number)
                
            elif convert_message_to == "decode":
                return convert_message_to_decode(letters_index, i , shift_number)

def create_message(convert_message_to:str, letters_index:list[str]) -> None:
    '''
    Create message and the computer will encrypt/decrypt for you
    Eveytime its looping it will concat the letters in convert_message_to_secret to genertae the message 
    
    parameters: 
        - convert_message_to:str
        - letters_index:list[str]
    
    returns string
    '''
    print("Type your message:")
    message:str = input("")
    print("Type the shift number:")
    shift_number:int = int(input(""))
    convert_message_to_secret:str = ""
    for ind in range(0,len(message),1):
        current_letter:str = message[ind]
        convert_message_to_secret = convert_message_to_secret + letter_position(letters_index , convert_message_to , shift_number , current_letter)
    print(f"Here's the result: '{convert_message_to_secret}'.")
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
        if type_word == "encode" or type_word == "decode":
            create_message(convert_message_to=type_word,letters_index=letters)

        else:
            print ("Type the word correctly")
            continue

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break
        elif yes_no == "yes":
            continue
        
def main() -> None:
    play()
    
if __name__ == '__main__': 
    main()
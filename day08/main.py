
letters:list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def funct_input() -> None:
    while True:
        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        type_word:str = input("")
        if type_word == "encode":
            print("Type your message:")
            message:str = input("")
            print("Type the shift number:")
            shift_number:int = int(input(""))
            print(f"Here's the encoded result: {message}")
        elif type_word == "decode":
            print("Type your message:")
            message:str = input("")
            print("Type the shift number:")
            shift_number:int = int(input(""))
            print(f"Here's the encoded result: secret message")
        else:
            print("Write the words correctly")
            continue  # Go back to the beginning of the loop

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break

funct_input()


    
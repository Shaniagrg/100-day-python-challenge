
letters:list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def funct_input() -> None:
    while True:
        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        type_word:str = input("")
        
        if type_word == "encode":
            print("Type your message:")
            message:str = input("")
            print("Type the shift number:")
            shift_number:int = int(input(""))

            encrypt:list[str] = []

            for ind in range(0,len(message),1):
                current_letter:str = message[ind]
                for i in range(0,len(letters),1):
                    if current_letter == letters[i]:   
                        secret:int = (i + shift_number) % 26   #26 cuz theres 26 letter in total when yp type z it will wrap back to 'a'
                        print(secret)
                        encrypt.append(letters[secret])
            
            print(f"Here's the encoded result: {''.join(encrypt)}")
        elif type_word == "decode":
            print("Type your message:")
            message:str = input("")
            print("Type the shift number:")
            shift_number:int = int(input(""))

            decrypt: list[str] = []

            for ind in range(0, len(message), 1):
                current_letter = message[ind]
                for i in range(0, len(letters), 1):
                    if current_letter == letters[i]:   
                        secret: int = (i - shift_number) % 26  # minus - shift backward
                        decrypt.append(letters[secret])

            print(f"Here's the decoded result: {''.join(decrypt)}")
        else:
            print("Write the words correctly")
            continue  # Go back to the beginning of the loop

        print("Do you want to run this program again?")
        yes_no:str = input("Type 'yes' or 'no': ")
        if yes_no == "no":
            print("Goodbye")
            break

funct_input()

import random
while True:
    def end_game(sum_my_card:int,sum_computer_card:int) -> None:

        '''
        - compare the sum and declare the winner

        parameter:
            - sum_my_card:int
            - sum_computer_card:int

        return:
                - None
        '''
        if sum_my_card > sum_computer_card:
            print("You Win!!!")
        elif sum_my_card < sum_computer_card:
            print("You lost =(")
    
    def ace_conversion(convert:list[str]) -> str:
            '''
            till here the list[str] its still string

            - sum the total value from convert[list[str]] and store in total_value type int
            - use total_value to determine the value of ace
            - store the ace value in ace_value_determine as string 

            parameter:
                - convert:list[str]

            return:
                - string
            
            '''
            total_value:int = 0
            ace_value_determine:str = ""

            for i in range(0,len(convert),1):
                if convert[i] == "ace":
                    continue
                elif convert[i] == "jack" or convert[i] == "queen" or convert[i] == "king":
                    total_value = total_value + 10
                else:
                    total_value = total_value + int(convert[i])


            if total_value <= 10:
                ace_value_determine = "11"
                return ace_value_determine
            elif total_value > 11:
                ace_value_determine = "1"
                return ace_value_determine

    def convert_value(convert:list[str]) -> list[int]:
        '''
        - convert the jack,queen and king to "10" and ace to "11" or "1" in strings 
        - then type converion from list[string] to list[int]

        parameters:
            - convert:list[str]

        return:
            - list[int]
        '''

        for i in range(0,len(convert),1):
            if convert[i] == "jack" or convert[i] == "queen" or convert[i] == "king":
                convert[i] = "10"
            elif convert[i] == "ace":
                convert[i] = ace_conversion(convert)

        for ind in range(0,len(convert),1):
            convert[ind] = int(convert[ind])
        return convert
    
    def get_random_value(deck_map:dict[str, list[str]],used_cards:list[list[str]]) -> str:

        '''
        - ramdomly choose 2 values out from the 4 ramdom keys for both computer and user

        parameter:
            - deck_map:dict[str, list[str]]
            - used_cards:list[list[str]]

        return
            - string
        '''
        while True:
            random_key:str = random.choice(list(deck_map.keys()))
            random_value:str = random.choice(deck_map[random_key])
            random_key_value:list[str] = [random_key,random_value]
            if random_key_value in used_cards:
                continue
            else:
                used_cards.append(random_key_value)
                return random_value

    def append_value(deck_map:dict[str, list[str]],used_cards:list[list[str]], adding_card:dict[str, list[str]]) -> None:

        '''
        - call function get_random_value to get random value
        - append random_value to the my_card and convert to int

        parameter:
            - deck_map:dict[str, list[str]]
            - used_cards:list[list[str]]
            - adding_card:dict[str, list[str]]

        return:
            -  None
        '''
        append_random_value:str = get_random_value(deck_map,used_cards)
        adding_card["hand1"].append(append_random_value)
        convert_value(adding_card["hand1"])

    def split_check(deck_map:dict[str, list[str]],used_cards:list[list[str]],my_card:dict[str, list[int]], computer_card:list[int]) -> dict[str, list[int]]:

        '''
        - when user gets same card ask for split/add/pass
        - if split: user will have 2 individual cards instead of one
        - if add: just append calling append_value function
        - if pass: stay at it is

        parameter:
            - deck_map:dict[str, list[str]]
            - used_cards:list[list[str]]
            - my_card:dict[str, list[int]]

        return:
            -  dict[str, list[int]]
        '''
        if my_card["hand1"][0] == my_card["hand1"][1]:
            continue_game:str = input("Type 'y' to get another card, type 'n' to pass, type 's' to split: ")
            if continue_game == "s":
                split_transfer: str = my_card["hand1"].pop()
                my_card["hand2"] = [split_transfer]
                return my_card
            elif continue_game == "y":
                my_card = append_value(deck_map,used_cards,my_card)
                return my_card
            elif continue_game == "n":
                sum_my_card = sum_cards(my_card["hand1"])
                sum_computer_card = sum_cards(computer_card)
                end_game(sum_my_card,sum_computer_card)
            
    def sum_cards(sum:list[int]) -> int:
        '''
        - sum the cards 

        parameters:
            - sum:list[int]
        return:
            - int
        
        '''
        sum_cards_value:int = 0
        for i in range(0,len(sum),1):
            sum_cards_value = sum_cards_value + sum[i]
        return sum_cards_value


    def check_21(user:list[str],dealer:list[str]) -> str:

        '''
        - call function convert the value for jack,queen,ace and king
        - call function to sum the card to check if its over 21 or not

        parameter:
            - user:list[str]
            - dealer:list[str]
        
        return:
            - string

        '''
        dealer_convert_to_int:list[int] = convert_value(convert=dealer)
        user_convert_to_int:list[int] = convert_value(convert=user)

        user_total:int = sum_cards(sum=user_convert_to_int)
        dealer_total:int = sum_cards(sum=dealer_convert_to_int)

        if user_total > 21:
            return "You lost"
        elif dealer_total > 21:
            return "You Win!!!"
        
    def play(deck_map:dict[str, list[str]]) -> None:

        '''
        - loop function append_value to get 2 values for computer/user
        - create a variable to store used_cards to avoid repetition
        - call funtion to continue/split/end game

        parameters
            - deck_map
        return
            -  None
        '''
        used_cards:list[list[str]]= []
        computer_card:dict[str, list[str]] = {"hand1": []}
        my_card:dict[str, list[str]] = {"hand1": []}


        ######## Receive 2 cards for each #########


        for i in range (0,2,1):
            append_value(deck_map,used_cards,adding_card=my_card)
            append_value(deck_map,used_cards,adding_card=computer_card)

        print(f"Your cards: {my_card}")
        print(f"The computer's first card: {computer_card['hand1'][0]}")


        ########### check 21 in initial phase ########
        ######    here user/dealer value has chnaged to string -> int   ########

        initial_21_check:str = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])
        if initial_21_check == "You lost":
            print("You lost the game")
        elif initial_21_check == "You Win!!!":
            print("You won the game")
        

        ##########    split    ############

        my_card = split_check(deck_map,used_cards,my_card,computer_card["hand1"])
        print(my_card)

        #continue_game:str = input("Type 'y' to get another card, type 'n' to pass: ")
        
    def main() -> None:
        '''
        Create a map for all the cards 
        Also create pairs for split

        parameters:
            - None
        
        return:
            None
        '''
        print("Lets play blackjack")
        deck: dict[str, list[str]] = { 
            'Hearts': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
            'Diamonds': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
            'Clubs': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
            'Spades': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
        }
        print (play(deck))
        

    if __name__ == '__main__': 
            main()
        

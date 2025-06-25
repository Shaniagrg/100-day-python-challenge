import random

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


def split_check(my_card:dict[str, list[int]], computer_card:list[int]) -> str:

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
            return "split"
        elif continue_game == "y":
            append_value(my_card,add_on_hand=continue_game)
            return "no split"
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

def convert_value(convert:list[str]) -> bool:
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
    return True

def check_21(user:list[str],dealer:list[str]) -> bool:

    '''
    - call function convert the value for jack,queen,ace and king
    - call function to sum the card to check if its over 21 or not

    parameter:
        - user:list[str]
        - dealer:list[str]
    
    return:
        - string

    '''
    '''
    dealer_convert_to_int:list[int] = convert_value(convert=dealer)
    user_convert_to_int:list[int] = convert_value(convert=user)

    user_total:int = sum_cards(sum=user_convert_to_int)
    dealer_total:int = sum_cards(sum=dealer_convert_to_int)

    if user_total > 21:
        return "You lost"
    elif dealer_total > 21:
        return "You Win!!!"
    
    '''

    convert_value(convert=dealer)
    convert_value(convert=user)

    user_total:int = sum_cards(sum=dealer)
    dealer_total:int = sum_cards(sum=user)

    if user_total == 21:
        print("You Win!!!")
        return True
    elif dealer_total == 21:
        print ("You lost")
        return True
    else:
        return False

def get_random_value() -> str:

    '''
    - ramdomly choose 2 values out from the 4 ramdom keys for both computer and user
    - create a variable to store used_cards to avoid repetition
    parameter:
        - deck_map:dict[str, list[str]]
        - used_cards:list[list[str]]

    return
        - string
    '''
    deck_map: dict[str, list[str]] = { 
        'Hearts': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Diamonds': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Clubs': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"],
        'Spades': ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
    }
    used_cards:list[list[str]]= []
    while True:
        random_key:str = random.choice(list(deck_map.keys()))   #('hearts','diamonds','clubs', 'spades') => ['hearts','diamonds','clubs', 'spades'] & then random
        random_value:str = random.choice(deck_map[random_key])
        random_key_value:list[str] = [random_key,random_value]
        if random_key_value in used_cards:
            continue
        else:
            used_cards.append(random_key_value)
            return random_value

def append_value(adding_card:dict[str, list[str]], add_on_hand:str) -> bool:

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
    if add_on_hand == "y":
        append_random_value:str = get_random_value()
        adding_card["hand1"].append(append_random_value)
        #convert_value(adding_card["hand1"])
        return True
    elif add_on_hand == "yes2":
        append_random_value:str = get_random_value()
        adding_card["hand2"].append(append_random_value)
        #convert_value(adding_card["hand2"])
        return True
    elif add_on_hand == "yes1":
        append_random_value:str = get_random_value()
        adding_card["hand1"].append(append_random_value)
        convert_value(adding_card["hand1"])
        return True
    elif add_on_hand == "yes":
        append_random_value:str = get_random_value()
        for key,value in adding_card.items():
            adding_card[key].append(append_random_value)
            #convert_value(adding_card[key])
        return True
        
def play() -> None:

    '''
    - loop function append_value to get 2 values for computer/user
    - call funtion to continue/split/end game

    parameters
        - deck_map
    return
        -  None
    '''

    computer_card:dict[str, list[str]] = {"hand1": []}
    my_card:dict[str, list[str]] = {"hand1": []}

    ######## Receive 2 cards for each #########

    for i in range (0,2,1):
        append_value(adding_card=my_card,add_on_hand="y")
        append_value(adding_card=computer_card,add_on_hand="y")

    print(f"Your cards: {my_card}")
    print(f"The computer's first card: {computer_card['hand1'][0]}")


    ########### check 21 in initial phase ########
    ######    here user/dealer value has chnaged to string -> int   ########
    '''
    initial_21_check:str = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])
    if initial_21_check == "You lost":
        print("You lost the game")
    elif initial_21_check == "You Win!!!":
        print("You won the game")
    '''
    while True:
        winner_decide_for_21 = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])  #value had convertered into list[int]
        if winner_decide_for_21 == True:
            break

        ##########    split    ############
    
        option_to_split:str = split_check(my_card,computer_card["hand1"])
        if option_to_split == "split":
            print(f"Your first individual card [{my_card['hand1']}] and your second individual card {my_card['hand2']}")
            while True:
                continue_game:str = input("Type 'yes1' to get another card for first hand, 'yes2' to get another card for second hand, 'yes' to get another card for both hand, type 'n' to pass: ")
                if continue_game == "yes1":
                    user_choice:str = "yes1"
                    append_value(adding_card=my_card,add_on_hand=user_choice)
                    winner_decide_for_21:bool = check_21(user=str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
                    
                    if winner_decide_for_21 == True:

                        print("If you still want to continue.")
                        while True:
                            continue_game = input("Type 'yes2' to get another card for second hand, 'yes' to get another card for both hand, type 'n' to pass: ")
                            if continue_game == "yes2":
                                user_choice: str = "yes2"
                                append_value(adding_card=my_card,add_on_hand=user_choice)
                                winner_decide_for_21 = check_21(user = str(my_card["hand2"]), dealer=str(computer_card["hand1"]))
                                if winner_decide_for_21 == True:
                                    break
                                else:
                                    continue
                        break
                    elif winner_decide_for_21 == False:
                        continue   


                elif continue_game == "yes2":
                    user_choice: str = "yes2"
                    append_value(adding_card=my_card,add_on_hand=user_choice)
                    winner_decide_for_21:bool = check_21(user=str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
                    if winner_decide_for_21 == True:
                        print("If you still want to continue.")
                        while True:
                            continue_game = input("Type 'yes1' to get another card for first hand, 'yes' to get another card for both hand, type 'n' to pass: ")
                            if continue_game == "yes1":
                                user_choice: str = "yes1"
                                append_value(adding_card=my_card,add_on_hand=user_choice)
                                winner_decide_for_21 = check_21(user = str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
                                if winner_decide_for_21 == True:
                                    break
                                else:
                                    continue
                        break
                    elif winner_decide_for_21 == False:
                        continue 


                elif continue_game == "yes":

                    user_choice: str = "yes"
                    while True:
                        append_value(adding_card=my_card,add_on_hand=user_choice)
                        winner_decide_for_21 = check_21(user = str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
                        if winner_decide_for_21 == True:
                            break
                        winner_decide_for_21 = check_21(user = str(my_card["hand2"]), dealer=str(computer_card["hand1"]))
                        if winner_decide_for_21 == True:
                            break
                    break

        elif option_to_split == "no split":
            continue_game_ask = input("Type 'y' to add another card or type 'n' to pass") 
            if continue_game_ask == 'y':
                append_value(adding_card=my_card,add_on_hand=user_choice)
                winner_decide_for_21:bool = check_21(user=str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
            else:
                user_total:int = sum_cards(sum=my_card['hand1'])
                dealer_total:int = sum_cards(sum=computer_card["hand1"])
                end_game(sum_my_card=user_total, sum_computer_card=dealer_total)
            break
        
        while True:
            continue_game = input("Type 'y' to add another card or type 'n' to pass: ")
            if continue_game == 'y':
                append_value(adding_card=my_card,add_on_hand='y')
                winner_decide_for_21:bool = check_21(user=str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
                if winner_decide_for_21 == True:
                    break
                else:
                    continue
                
            elif continue_game == 'n':
                user_total:int = sum_cards(sum=my_card['hand1'])
                dealer_total:int = sum_cards(sum=computer_card["hand1"])
                end_game(sum_my_card=user_total, sum_computer_card=dealer_total)
                break
        break



        
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
    
    print (play())
    

if __name__ == '__main__': 
        main()
    

import random
def condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand:str,user_choice) -> str:
    
    deleted_card:list[str] = []
    if 'hand1' in user_card_splited or 'hand2' in user_card_splited:
        convert_dealer_for_total:list[str] = convert_value(computer_card_split_check_with_user['hand1'])
        dealer_total_decide:int = sum_cards(convert_dealer_for_total)

        convert_user_for_total:list[str]  = convert_value(user_card_splited[user_hand])
        user_total_for_winner:int = sum_cards(convert_user_for_total)
        winner:str = ""

        if user_choice == "yes" or user_choice == "yes1" or user_choice == "yes2":
            winner_decide_for_21 = check_21(user=user_card_splited[user_hand], dealer=computer_card_split_check_with_user['hand1'])

            if winner == "You Win!!!" or winner_decide_for_21 == "You Win!!!":
                print(f"You won!!!!! {user_hand}: {user_card_splited[user_hand]}")
                deleted_card = user_card_splited.pop(user_hand)
                print(f"Your {user_hand}: {deleted_card} card has been deleted")
                return user_hand
            elif winner == "You lost =(" or winner_decide_for_21 == "You lost":
                print(f"You lost  {user_hand}: {user_card_splited[user_hand]}")
                deleted_card = user_card_splited.pop(user_hand)
                print(f"Your {user_hand}: {deleted_card} card has been deleted")
                return user_hand
            elif winner_decide_for_21 == "continue":
                return "continue"
        
        elif user_choice == 'n':
            if 'hand1' in user_card_splited and 'hand2' in user_card_splited :
                winner = end_game(sum_my_card=user_total_for_winner, sum_computer_card=dealer_total_decide)
                print(f"{winner}  user_card:  {user_card_splited[user_hand]} ")
                return "End game"
            elif 'hand1' in user_card_splited:
                winner = end_game(sum_my_card=user_total_for_winner, sum_computer_card=dealer_total_decide)
                print(f"{winner}  hand1: {user_card_splited[user_hand]} ")
                return "End game for hand1"
            elif 'hand2' in user_card_splited:
                winner = end_game(sum_my_card=user_total_for_winner, sum_computer_card=dealer_total_decide)
                print(f"{winner}  hand2: {user_card_splited[user_hand]} ")
                return "End game for hand2"

def decesion(my_card,computer_card) -> None:
    while True:
            continue_game = input("Type 'y' to add another card or type 'n' to pass: ")
            if continue_game == 'y':
                append_value(adding_card=my_card,add_on_hand='y')
                print(f"your card is {my_card}")
                winner_decide_for_21:str = check_21(user=my_card["hand1"], dealer=computer_card["hand1"])
                #end_game(sum_my_card=user_total, sum_computer_card=dealer_total)
                if winner_decide_for_21 == "You Win!!!":
                    print("You won!!!!!")
                    break
                elif winner_decide_for_21 == "You lost":
                    print("You lost")
                    break
                elif winner_decide_for_21 == "continue":
                    continue
                
            elif continue_game == 'n':
                print(f"My card is: {my_card}")
                #print(f"Computer card is: {computer_card}")
                convert_user_for_total:list[str] = convert_value(my_card["hand1"])
                convert_dealer_for_total:list[str] = convert_value(computer_card["hand1"])

                user_total_for_winner:int = sum_cards(convert_user_for_total)
                dealer_total_decide:int = sum_cards(convert_dealer_for_total)

                winner = end_game(sum_my_card=user_total_for_winner, sum_computer_card=dealer_total_decide)
                if winner == "You Win!!!":
                    #print(f"Computer total was [{dealer_total_decide}] and user total was [{user_total_for_winner}]")
                    print("You won!!!!!")
        
                elif winner == "You lost =(":
                    print(f"Computer total was [{dealer_total_decide}] and user total was [{user_total_for_winner}]")
                    print("You lost")
                
                break
 
def split(user_card_splited,computer_card_split_check_with_user) -> None:
    
    while True:
        if len(user_card_splited) == 0:  #map is empty then game over
            print("Game over")
            return 
        continue_game:str = input("Type 'yes1' to get another card for first hand, 'yes2' to get another card for second hand, 'yes' to get another card for both hand, type 'n' to pass: ")
        received_user_card:str = ""
        if continue_game == "yes1" and 'hand1' in user_card_splited:
            user_choice = "yes1"
            append_value(adding_card = user_card_splited,add_on_hand = user_choice)
            user_hand:str = 'hand1'
            received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
            #print(f"My card: {user_card_splited}")
        elif continue_game == "yes2" and 'hand2' in user_card_splited:
            user_choice = "yes2"
            append_value(adding_card = user_card_splited,add_on_hand = user_choice)
            user_hand:str = 'hand2'
            received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
            #print(f"My card: {user_card_splited}")
        #remove_hand:str = ""
        elif continue_game == "yes":
            if 'hand1' in user_card_splited:
                user_choice = "yes1"
                append_value(adding_card = user_card_splited,add_on_hand = user_choice)
                user_hand:str = 'hand1'
                received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
            if 'hand2' in user_card_splited:
                user_choice = "yes2"
                append_value(adding_card = user_card_splited,add_on_hand = user_choice)
                user_hand:str = 'hand2'
                received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
            #print(f"My card: {user_card_splited}")
        for key in user_card_splited:
            if received_user_card == "hand1" and key in user_card_splited:
                continue_game = input("Type 'yes2' to get another card for second hand or type 'n' to pass: ")
            elif received_user_card == "hand2" and key in user_card_splited:
                continue_game = input("Type 'yes1' to get another card for first hand or type 'n' to pass: ")
            elif key not in user_card_splited:
                print ("End Game")
                break
            elif received_user_card == "continue":
                continue
        if continue_game == "n":
            print(f"My card: {user_card_splited}")
            user_choice = "n"
            if 'hand1' in user_card_splited:
                
                user_hand:str = 'hand1'
                received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
                print(received_user_card)
            if 'hand2' in user_card_splited:
                
                user_hand:str = 'hand2'
                received_user_card = condition_after_split(user_card_splited,computer_card_split_check_with_user,user_hand,user_choice)
                print(received_user_card)
            print("Game Over")
            break

def end_game(sum_my_card:int,sum_computer_card:int) -> str:

    '''
    - compare the sum and declare the winner

    parameter:
        - sum_my_card:int
        - sum_computer_card:int

    return:
            - None
    '''
    if sum_my_card > sum_computer_card:
        print(f"Computer total was [{sum_computer_card}] and user total was [{sum_my_card}]")
        return "You Win!!!"
    elif sum_my_card < sum_computer_card:
        print(f"Computer total was [{sum_computer_card}] and user total was [{sum_my_card}]")
        return "You lost =("
    

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
        continue_game:str = input("Type 's' to split or type 'c' to continue: ")
        if continue_game == "s":
            split_transfer: str = my_card["hand1"].pop()
            my_card["hand2"] = [split_transfer]
            print(f"Your user card have 2 hands now {my_card}")
            return "split"
        
        elif continue_game == "c":
            return "continue"

def sum_cards(card_received_by_players:list[str]) -> int:
    '''
    - sum the cards 

    parameters:
        - sum:list[int]
    return:
        - int
    
    '''
    sum_cards_value:int = 0

    for i in range(0,len(card_received_by_players),1):
        sum_cards_value = sum_cards_value + int(card_received_by_players[i])
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

def convert_value(convert:list[str]) -> list[str]:
    '''
    - convert the jack,queen and king to "10" and ace to "11" or "1" in strings 
    - then type converion from list[string] to list[int]

    parameters:
        - convert:list[str]

    return:
        - list[int]
    '''
    converted_int_str: list[str]= []
    change_value:str = ""
    for i in range(0,len(convert),1):
        if convert[i] == "jack" or convert[i] == "queen" or convert[i] == "king":
            change_value = "10"
            converted_int_str.append(change_value)
        elif convert[i] == "ace":
            change_value = ace_conversion(convert)
            converted_int_str.append(change_value)
        else:
            converted_int_str.append(convert[i])
    return converted_int_str

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

    dealer_converted_int_str:list[str] = convert_value(convert=dealer)
    user_converted_int_str:list[str] = convert_value(convert=user)

    user_total:int = sum_cards(card_received_by_players= user_converted_int_str)
    dealer_total:int = sum_cards(card_received_by_players=dealer_converted_int_str)

    if user_total == 21 or dealer_total > 21: 
        print(f"your card is total is [{user_total}] and computer card is [{dealer_total}]")
        return "You Win!!!"
    elif dealer_total == 21 or user_total > 21:
        print(f"your card is total is [{user_total}] and computer card is [{dealer_total}]")
        return "You lost"
    else:
        return "continue"

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
        #convert_value(adding_card["hand1"])
        return True
    
    elif add_on_hand == "yes":
        for key in adding_card:
            if key == "hand1":
                append_random_value:str = get_random_value()
                adding_card["hand1"].append(append_random_value)
            elif key == "hand2":
                append_random_value:str = get_random_value()
                adding_card["hand2"].append(append_random_value)
    
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
    '''
    initial_21_check:str = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])
    if initial_21_check == "You lost":
        print("You lost the game")
    elif initial_21_check == "You Win!!!":
        print("You won the game")
    '''
    while True:
        winner_decide_for_21 = check_21(user=my_card["hand1"],dealer=computer_card["hand1"])  
        if winner_decide_for_21 == True:
            break

        ##########    split    ############
    
        option_to_split:str = split_check(my_card,computer_card["hand1"])
        
        if option_to_split == "split":
            split(user_card_splited=my_card,computer_card_split_check_with_user=computer_card)
            break

        decesion(my_card,computer_card)
        break
            
        '''
        elif option_to_split == "no split":
            continue_game_ask = input("Type 'y' to add another card or type 'n' to pass") 
            if continue_game_ask == 'y':
                append_value(adding_card=my_card,add_on_hand= "y")
                winner_decide_for_21 = check_21(user=str(my_card["hand1"]), dealer=str(computer_card["hand1"]))
            else:
                decesion(my_card,computer_card)
            break
        '''
        
        
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
    
    play()
    

if __name__ == '__main__': 
        main()
    

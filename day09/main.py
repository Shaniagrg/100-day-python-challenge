

def total_bidders(all_bidders_record:dict[str,float]) -> None:
    
    '''
    Use the all_bidders_record as refrence to know the winner
    Store the highest bid everytime you compare with the name 
    Check serially 1st iteration then 2nd until the end of the map
    Then store the highest bidder and declare

    parameters:
        - all_bidders_record:dict[str,float]

    returns: bool
    '''
    highest_bid:float = 0.0
    winner_name:str = ""
    for key,value in all_bidders_record.items():
        if value > highest_bid:
            highest_bid = value
            winner_name = key
    print(f"The highest bidder is {winner_name} with a ${highest_bid}.")
    print("Thank you for participation.")
    return 


def play(bidders_record:dict[str,float]) -> None:
    '''
    Start the bidding

    parameters:
        - bidders_record:dict[str,float]

    return: None
    '''
    while True:
    
        name:str = input("What is your name?: ")
        bid_price:float = float(input("How much would you like to bid?: $"))
        bidders_record[name] = bid_price
        
        print("Are there any other bidders for this auction? Type 'yes' or 'no'.")
        other_bidders:str = input()
        
        if other_bidders == "no":
            total_bidders(bidders_record)
            break
        elif other_bidders == "yes":
            continue        
        return
def main() -> None:
    print("Welcome to the private bidding auction")
    bidders:dict[str,float] = {}
    play(bidders)
    
if __name__ == '__main__': 
    main()

#yes then continue the loop and no then the end of the bid with thank you message 
# map name:bid_price
# list 
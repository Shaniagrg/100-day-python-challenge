def winner_check(all_bidders_record:dict[str,float], compare_bids:float, save_winner_name:str) -> None:
        for key,value in all_bidders_record.items():
            if value > compare_bids:
                compare_bids = value
                save_winner_name = key
        print(f"The highest bidder is {save_winner_name} with a ${compare_bids}.")
        print("Thank you for participation.")
     

def total_bidders(all_bidders_record:dict[str,float]) -> bool:
        highest_bid:float = 0.0
        winner_name:str = ""
        winner_check(all_bidders_record, compare_bids=highest_bid, save_winner_name=winner_name)
        return True


def play(bidders_record:dict[str,float]) -> None:

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

def main() -> None:
    print("Welcome to the private bidding auction")
    bidders:dict[str,float] = {}
    play(bidders)
    
if __name__ == '__main__': 
    main()

#yes then continue the loop and no then the end of the bid with thank you message 
# map name:bid_price
# list 
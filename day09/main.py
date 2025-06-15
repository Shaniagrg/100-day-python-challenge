def play(bidders_record):

    while True:
    
        name:str = input("What is your name?: ")
        bid_price:float = float(input("How much would you like to bid?: $"))
        bidders_record[name] = bid_price
        #print(bidders)
        
        print("Are there any other bidders for this auction? Type 'yes' or 'no'.")
        other_bidders:str = input()
        
        if other_bidders == "no":
            
            highest_bid:float = 0.0
            winner_name:str = ""
            for key,value in bidders_record.items():
                if value > highest_bid:
                    highest_bid = value
                    winner_name = key
            print(f"The highest bidder is {winner_name} with a ${highest_bid}.")
            print("Thank you for participation.")
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
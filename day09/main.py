print("Welcome to the private bidding auction")

bidders:dict[str,float] = {}
highest_bid:float = 0.0
highest_bidder:dict[str,float] = {}

while True:
   

    name:str = input("What is your name?: ")
    bid_price:float = float(input("How much would you like to bid?: $"))
    bidders[name] = bid_price
    #print(bidders)
    
    print("Are there any other bidders for this auction? Type 'yes' or 'no'.")
    other_bidders:str = input()
    
    if other_bidders == "no":
        for key,value in bidders.items():
            if bidders[name] > highest_bid:
                highest_bid = bidders[name]
                if value == highest_bid:
                    winner_name:str = key
        print(f"The highest bidder is {winner_name} with a ${highest_bid}.")
        print("Thank you for participation.")
        break
    elif other_bidders == "yes":
        continue        


#yes then continue the loop and no then the end of the bid with thank you message 
# map name:bid_price
# list 
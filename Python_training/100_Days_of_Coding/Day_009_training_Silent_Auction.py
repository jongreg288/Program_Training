import os

auction_dict = {
	"Names" : [],
	"Bids" : []
}

def bid_start():
	bidder_name = input("What is your name?: ")
	bidder_price = input("What is your bid?: $")
	while not bidder_price.isdigit():
		bidder_price = input("Please enter a valid number for the bid: $")
	auction_dict["Names"].append(bidder_name)
	auction_dict["Bids"].append(bidder_price)
	more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
	if more_bidders == "yes":
		os.system('cls' if os.name == 'nt' else 'clear')
		bid_start()
	elif more_bidders == "no":
		os.system('cls' if os.name == 'nt' else 'clear')
		highest_bid()
	else:
		print("Please type 'yes' or 'no'.")
		bid_start()

def highest_bid():
	max_bid = 0
	winner = ""
	max_bid = max([int(bid) for bid in auction_dict["Bids"]])
	winner_index = auction_dict["Bids"].index(str(max_bid))
	print(f"The winner is {auction_dict["Names"][winner_index]} with a bid of ${max_bid}.")

if __name__ == "__main__":
	bid_start()

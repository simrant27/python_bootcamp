from art import logo
# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print(logo)


def max_bidder(bid_dict):
    max_bid = 0
    name_of_bidder = ""
    for bid in bid_dict:
        if bid_dict[bid] > max_bid:
            max_bid = bid_dict[bid]
            name_of_bidder = bid

    print(f"Max bid is {max_bid} by {name_of_bidder}")

bidder = {}
more_bidder = "yes"
while more_bidder == "yes":
    name = input("Enter your name: ")
    bid_amt = int(input("Enter your bid amount: "))
    bidder[name] = bid_amt
    more_bidder = input("Enter if there is more bidder, enter yes and no: ").lower()
    if more_bidder == "yes":
        print("\n")
    else:
        max_bidder(bidder)

# print(bidder)



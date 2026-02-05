continue_bidding = True
bids = {}
# def find_highest_bidder(bids):
#     winner=""
#     max_bid = 0
#
#     for bidder in bids:
#         bid_amt=bids[bidder]
#         if bid_amt > max_bid:
#             max_bid = bid_amt
#             winner = bidder
#     print(f"The highest bid is {winner} with a bid of ${max_bid}")
while continue_bidding:
    bidder_name = input("Enter your name: ")
    bid = int(input("Enter your price: "))
    bids[bidder_name] = bid
    auction_on = input("Are there any more bids? y/n: ").lower()
    if auction_on=="n":
        highest_bid=max(bids,key=bids.get,)
        print(f"The winner is {highest_bid} with a bid of ${bids[highest_bid]}")
        continue_bidding = False
        # find_highest_bidder(bids)
    elif auction_on=="y":
        print("\n"*15)




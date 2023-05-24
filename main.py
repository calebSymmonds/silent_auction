from replit import clear
from art import logo
bids = {}
next = True
print(logo)
print("Welcome to the silent auction.")

def highest_bidder (bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while next == True:
  name = input("What is your name?\n")
  price = int(input("What is your bid?\n$"))
  bids[name] = price
  next2 = input("Would you like to continue? (Yes or No)\n").lower()
  if next2 == "no":
    next = False
    highest_bidder(bids)
  elif next2 == "yes":
    clear()
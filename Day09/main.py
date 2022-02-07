from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}
repeat = True

while(repeat == True):
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bids[name] = bid

  keep_bidding = input("Are there other bidders? Type 'yes' or 'no'").lower()
  if keep_bidding == "yes":
    repeat=True
  elif keep_bidding == "no":
    repeat = False
  else:
    repeat = False
  clear()

max = 0
name_win = ""
for name in bids:
  if bids[name] > 0:
    max = bids[name]
    name_win = name
print(f"The winner is {name_win} with a bid of ${max}") 

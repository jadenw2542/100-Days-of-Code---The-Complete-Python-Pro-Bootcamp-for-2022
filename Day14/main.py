from art import logo, vs
from game_data import data
import random

print(logo)
def print_data(object):
  print(f"{object['name']}, {object['description']}, {object['country']}")

def check_answer(a, b, guess):
  if guess == "A" and a['follower_count'] > b['follower_count']:
    return True
  elif guess == "B" and a['follower_count'] < b['follower_count']:
    return False
  else:
    return 0

database = data
current_score = 0
a_data = random.choice(database)
database.remove(a_data)
b_data = random.choice(database)
database.remove(b_data)
continue_game = True
while continue_game == True:
  print(f"Compare A: {print_data(a_data)}")
  print(vs)
  print(f"Compare B: {print_data(b_data)}")
  guess = input("Who has more Followers? Type 'A' or 'B'")
  answer = check_answer(a_data, b_data, guess)
  if answer == 0:
    continue_game = False
    print(f"Game Over, your score was {current_score}")
  else:
    current_score += 1
    if answer == False:
      a_data = b_data
    b_data = random.choice(database)
    database.remove(b_data)
    print(f"You're right! Current score is {current_score}\n\n")
  
    


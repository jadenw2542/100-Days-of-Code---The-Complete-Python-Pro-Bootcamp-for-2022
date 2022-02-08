#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
logo = '''  _______  __    __   _______     _______.     _______.   .___________. __    __   _______    .__   __.  __    __  .___  ___. .______    _______ .______       __  
 /  _____||  |  |  | |   ____|   /       |    /       |   |           ||  |  |  | |   ____|   |  \ |  | |  |  |  | |   \/   | |   _  \  |   ____||   _  \     |  | 
|  |  __  |  |  |  | |  |__     |   (----`   |   (----`   `---|  |----`|  |__|  | |  |__      |   \|  | |  |  |  | |  \  /  | |  |_)  | |  |__   |  |_)  |    |  | 
|  | |_ | |  |  |  | |   __|     \   \        \   \           |  |     |   __   | |   __|     |  . `  | |  |  |  | |  |\/|  | |   _  <  |   __|  |      /     |  | 
|  |__| | |  `--'  | |  |____.----)   |   .----)   |          |  |     |  |  |  | |  |____    |  |\   | |  `--'  | |  |  |  | |  |_)  | |  |____ |  |\  \----.|__| 
 \______|  \______/  |_______|_______/    |_______/           |__|     |__|  |__| |_______|   |__| \__|  \______/  |__|  |__| |______/  |_______|| _| `._____|(__)'''
EASY = 10
HARD = 5
print(logo)
def set_difficult():
  difficulty = input("Choose a difficulty: 'easy' or 'hard' ").lower() 
  if difficulty == "easy":
    return EASY
  elif difficulty == "hard":
    return HARD
  else:
    print("Not a valid difficulty")

print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
rand_num = random.randint(1,101)
guesses = set_difficult()
exit = False
print(f"You have {guesses} to find the number")
while guesses != 0 or exit == True:
  guess = int(input("Make a guess: "))
  if guess > rand_num:
    print("Too High")
    guesses -= 1
  elif guess < rand_num:
    print("Too low")
    guesses -= 1
  elif guess == rand_num:
    exit = True
    print(f"You got it! the answer was {rand_num}")
  print(f"You have {guesses} left")
  print("Guess again")
  
if exit == False:
  print("You've run out of guesses, you lose")
  
                                                                                                                                                                   












    


                                                                                                                                                                               
                                                                                    





                                                      

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if(user < 0) or (user > 2):
  print("Invalid Number, You Lose")
else:
  choices = [rock, paper, scissors]
  bot = random.choice([0, 1, 2])
  print(choices[user])
  print("Computer chose:")
  print(choices[bot])

  if(user == 0) and (bot == 2):
    print("You Win")
  elif(user == 1) and (bot == 0):
    print("You Win")
  elif(user == 2) and (bot == 1):
    print("You win")
  elif(user == bot): 
    print("Draw")
  else:
    print("You Lose")




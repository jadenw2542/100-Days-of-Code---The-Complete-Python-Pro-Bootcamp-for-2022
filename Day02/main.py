#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇8.
print("Welcome to the tip calculator!")
total = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip = float(tip) * .01 + 1
total = float(total) * tip
payment_person =  total / int(people)
#payment_person = round(payment_person,2)
payment_person = "{:.2f}".format(payment_person)
print("Each person should pay: $" + str(payment_person))
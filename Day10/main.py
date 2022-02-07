from art import logo
def add(n1,n2):
  return n1 + n2
def sub(n1, n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for op in operations:
    print(op)
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the first number?: "))

  answer = operations[operation_symbol](num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {answer}")

  repeat = True
  choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
  if choice == "y":
    repeat == True
  elif choice == "n":
    calculator()


  while repeat == True:
    operation_symbol = input("Pick an operation")
    num3 = int(input("What's the next number?: "))
    answer2 = operations[operation_symbol](answer, num3)
    print(f"{answer} {operation_symbol} {num3} = {answer2}")
    answer = answer2
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()
    if choice == "y":
      repeat == True
    elif choice == "n":
      calculator()
  
calculator()
    


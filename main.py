from art import logo
def add(number_1, number_2):
  return number_1 + number_2

def subtract(number_1, number_2):
  return number_1 - number_2

def multiply(number_1, number_2):
  return number_1 * number_2

def divide(number_1, number_2):
  return number_1 / number_2

def exponent(number_1, number_2):
  return number_1 ** number_2

operations = {
  "+": add,
  "-": subtract, 
  "*": multiply, 
  "/": divide,
  "**": exponent
}
def calculator():
  print(logo)
  number_1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
    
  continue_calculating = True
  while continue_calculating:
    operation_symbol = input("Choose and operation from the list above: ")
    number_2 = float(input("What's the next number?: "))
    result = operations[operation_symbol]
    answer = result(number_1, number_2)
    # if operation_symbol == "+":
    #   operations[operation_symbol] = add(number_1, number_2)
    # elif operation_symbol == "-":
    #   operations[operation_symbol] = subtract(number_1, number_2)
    # elif operation_symbol == "*":
    #   operations[operation_symbol] = multiply(number_1, number_2)
    # elif operation_symbol == "/":  
    #   operations[operation_symbol] = divide(number_1, number_2)
    # else:
    #   print("Invalid operation")
    print(f"{number_1} {operation_symbol} {number_2} = {answer}")
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calaculation ").lower()
    if again == "y":
      number_1 = answer
    else:
      continue_calculating = False
      calculator()
    
calculator()
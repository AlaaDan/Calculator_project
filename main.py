def add(number_1, number_2):
  return number_1 + number_2

def subtract(number_1, number_2):
  return number_1 - number_2

def multiply(number_1, number_2):
  return number_1 * number_2

def divide(number_1, number_2):
  return number_1 / number_2

operations = {
  "+": add,
  "-": subtract, 
  "*": multiply, 
  "/": divide
}

number_1 = int(input("What's the first number?: "))

for key in operations:
  print(key)

operation_symbol = input("Choose and operation from the list above: ")
number_2 = int(input("What's the second number?: "))
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
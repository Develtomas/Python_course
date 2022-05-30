#calc functions def
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

#fn dictionary
calculation_fn = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  """recursive calculator function"""
  num1 = float(input("First number > "))
  while True:
    num2 = float(input("Second number > "))
    
    for key in calculation_fn:
      print(key, end="\n")
    
    symbol = input('Pick the operation from above > ')
    
    #calc call
    result = calculation_fn[symbol](num1,num2)
    
    #print res
    print(f"{num1} {symbol} {num2} = {result}")
    
    #repeat
    again = input(f"'y' to continue with {round(result,2)}, otherwise - to start a new calculation: ")
    if again == 'y':
      num1 = result
      continue
    else: 
      print("___________________\n")
      calculator()

calculator()
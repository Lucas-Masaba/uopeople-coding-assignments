def divide():
  numerator = int(input("Enter the numerator: "))
  denominator = int(input("Enter the denominator: "))
    
  if denominator == 0:
    print("Error: Division by zero is not allowed in Python or Mathematics.")
  else:
    result = numerator / denominator
    print(result)
  
divide()

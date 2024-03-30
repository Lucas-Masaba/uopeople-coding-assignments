def countdown(n): 
    if n <= 0: 
        print('Blastoff!') 
    else: 
        print(n) 
        countdown(n-1) 

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)

def count():
    num = int(input("Enter a number: ")) # Ensure the input is an integer
    if num > 0:
        countdown(num)
    elif num < 0:
        countup(num)
    else:
        countdown(num)
        
count()
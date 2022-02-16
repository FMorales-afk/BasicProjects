#Calculator

#TODO writing unit tests to test all functions

def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
    if y == 0:
        print("Can't divide by zero!")
    else:
        return x / y
    
print("This is a calculator")
print("What would you like to do")
print("1 - ADD")
print("2 - SUBTRACT")
print("3 - MULTIPLY")
print("4 - DIVIDE")

while True:
    choice = input("Please enter a number corresponding to an operation: ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
        
        if choice == '1':
            print(num1, '+', num2, '=', add(num1,num2))
        if choice == '2':
            print(num1, '-', num2, '=', subtract(num1,num2))
        if choice == '3':
            print(num1, '*', num2, '=', multiply(num1,num2))
        if choice == '4':
            print(num1, '/', num2, '=', divide(num1,num2))

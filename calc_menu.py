import calculator as calculator
def printMenu():   
    print("This is a calculator")
    print("What would you like to do")
    print("1 - ADD")
    print("2 - SUBTRACT")
    print("3 - MULTIPLY")
    print("4 - DIVIDE")
    print("5 - EXIT")

while True:
    printMenu()
    choice = input("Please enter a number corresponding to an operation: ")
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))
        
        if choice == '1':
            print(num1, '+', num2, '=', calculator.add(num1,num2))
        if choice == '2':
            print(num1, '-', num2, '=', calculator.subtract(num1,num2))
        if choice == '3':
            print(num1, '*', num2, '=', calculator.multiply(num1,num2))
        if choice == '4':
            print(num1, '/', num2, '=', calculator.divide(num1,num2))
    else: print("Goodbye...") 
    break
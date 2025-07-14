#Basic Arithematic calculator





def calculator(n1, n2, operation):  
    if operation == '+' :
        return n1 + n2
    elif operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '/':
        if n2 != 0:
            return n1 / n2
        else:
            return "Error: Division by zero!"
    else :
        print("some error occur, please try again!")

n1 = float(input("Enter first(1) number-"))

n2 = float(input("Enter second(2) number-"))

opration = input('Chose which operation you should perform(+, -, *, /)-')

result = calculator(n1, n2, opration)

print('Result-', result)
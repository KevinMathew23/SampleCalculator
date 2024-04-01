def calc():
    while True:
        num1 = input("please enter first number or q to quit: ")
        if(num1 == 'q'):
            break
        num2 = input("please enter second number or q to quit: ")
        if(num2 == 'q'):
            break

        try:
            int(num1) and int(num2)
        except ValueError:
            print("non-number entered, please try again or q to quit")
            continue
        num1, num2 = float(num1), float(num2)
        operation = input("Please choose an operation by entering '+', '-', '*', or '/'. Use '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division.   ")
        if(operation == '+'):
            print(num1 + num2)
        elif(operation == '-'):
            print(num1 - num2)
        elif(operation == '*'):
            print(num1 * num2)
        elif(operation == '/'):
            if(num2 == 0):
                print("Undefined, Please Try Again")
                break
            print(num1 / num2)
        else:
            print("unknown symbol, please try again")
            continue
calc()
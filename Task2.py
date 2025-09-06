print("HLO, iam a Simple Calculator")
print("Type 'q' to quit")

while True:
    a = input("Enter your first number: ")
    if a == "q":
        break
    b = input("Enter your second number: ")
    op = input("Enter your operation ( [+] , [-] , [*] , [/] ): ")

    a = float(a)
    b = float(b)

    if op == "+":
        print(" Your answer is :", a + b)
    elif op == "-":
        print(" Your answer is :", a - b)
    elif op == "*":
        print(" Your answer is :", a * b)
    elif op == "/":
        if b != 0:
            print(" Your answer is :", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Its a Invalid operation")

        # here is a 1 line calculator for fun , simple and easy
        # while True: print(eval(input(">>>")))
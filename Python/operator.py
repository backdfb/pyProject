#4칙연산 계산기 프로젝트

playing = True

while playing:
    a = int(input("Choose a number:\n"))
    b = int(input("Choose another one:\n"))
    operation = input("Choose an operation:\n  Options are: +, -, *, or /.\n  Write 'exit' to finish.\n")

    if operation == "+":
        result = a + b
        print(result)
    elif operation == "-":
        result = a - b
        print(result)
    elif operation == "*":
        result = a * b
        print(result)
    elif operation == "/":
        if b == 0:
            print("Don't Use 0 in another one")
        else:
            result = a / b
            print(result)
    elif operation == "exit":
        print("See You Again.")
        playing = False
    else:
        print("Retry.")

print()

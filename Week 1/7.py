fn, op,sn = float(input("First number: ")), input("+ - * /: "),float(input("Second number: "))

if op == "/":
    if sn != 0:
        print(fn / sn)
    else:
        print("Error: division by zero")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
else:
    print("Unknown operation")
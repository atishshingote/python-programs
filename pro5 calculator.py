first = input("enter your first number : ")
oprator = input("enter your operator (+,-,*,/,%)")
second = input("enter yuor second number :")

first = int(first)
second = int(second)

if oprator == "+":
    print(first + second)

elif oprator == "-":
    print(first - second)

elif oprator == "*":
    print(first * second)

elif oprator == "/":
    print(first / second)

elif oprator == "%":
    print(first % second)

else:
    print("invalide operation")

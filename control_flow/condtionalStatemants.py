
is_male = True
is_single = True

if is_male and is_single:
    print("You are a male")
elif is_male and not(is_single):
    print("You are a short male")
else:
    print("You are a not male")


# Calculater

num1 = float(input("Enter number"))
op = input("Enter Operater")
num2 = float(input("Enter number"))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num)
else:
    print("Invaid operater")
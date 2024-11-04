# a = float(input())
# b = float(input())
# operation = character(input())

a = 2.0
b = 6.0
operation = '+'

if operation == '+':
    x = a + b
elif operation == '-':
    x = a - b
elif operation == '*':
    x = a * b
else:
    x = a / b

print("Result: ", x)

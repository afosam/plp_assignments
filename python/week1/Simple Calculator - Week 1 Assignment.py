# 🧮 Simple Unique Calculator

x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Choose (+, -, *, /): ")

if op == "+": 
    print(f"{x} + {y} = {x+y}")
elif op == "-": 
    print(f"{x} - {y} = {x-y}")
elif op == "*": 
    print(f"{x} * {y} = {x*y}")
elif op == "/": 
    print(f"{x} / {y} = {x/y}" if y != 0 else "❌ Cannot divide by zero")
else: 
    print("⚠️ Unknown operation")

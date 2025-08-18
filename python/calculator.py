a,b=float(input("First: ")),float(input("Second: "))
op=input("+, -, * or /: ")
r = a+b if op=="+" else a-b if op=="-" else a*b if op=="*" else a/b
print(f"{a} {op} {b} = {r}")

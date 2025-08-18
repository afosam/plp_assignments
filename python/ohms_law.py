# ohms_law.py
# V = I * R

# Ask the user for current (I) and resistance (R)
I = float(input("Enter the current (in A): "))
R = float(input("Enter the resistance (in ohms): "))

# Calculate voltage
V = I * R

# Show the result
print(f"The voltage is: {V} volts")

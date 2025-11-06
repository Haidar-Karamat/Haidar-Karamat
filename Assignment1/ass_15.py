num_1 = int(input("Enter first number="))
num_2 = int(input("Enter second number="))
print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    print(f"Addition is {num_1 + num_2}")
elif choice == '2':
    print(f"Subtraction is {num_1 - num_2}")
elif choice == '3':
    print(f"Multiplication is {num_1 * num_2}")
elif choice == '4' and num_2 != 0:
    print(f"Division is {num_1 / num_2}")
else:
    print("You make some mistake")

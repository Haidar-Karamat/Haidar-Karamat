#Temperature converter

#fah = 9/5 * (Celius) + 32
#Kelvin = Celius + 273.15
#Celius = 5/9 * (fah - 32)
#Celius = Kel - 273.15
#kelvin = 5/9 * (fah - 32) + 273.15
#fah = (kel - 273.15) * 9/5 + 32

def cel_to_fah(c):
    return (c * 9/5) + 32

def fah_to_cel(f):
    return (f - 32) * 5/9

def kel_to_cel(k):
    return k - 273.15

def cel_to_kel(c):
    return c + 273.15

def kel_to_fah(k):
    return (k - 273.15) * (9/5) + 32

def fah_to_kel(f):
    return (f - 32) * (5/9) + 273.15


print("Temperature Converter")
print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))
temp = float(input("Enter the temperature value: "))

if choice == 1:
    print("Result:", cel_to_fah(temp), "°F")
elif choice == 2:
    print("Result:", fah_to_cel(temp), "°C")
elif choice == 3:
    print("Result:", cel_to_kel(temp), "K")
elif choice == 4:
    print("Result:", kel_to_cel(temp), "°C")
elif choice == 5:
    print("Result:", fah_to_kel(temp), "K")
elif choice == 6:
    print("Result:", kel_to_fah(temp), "°F")
else:
    print("Invalid choice. Try again!")



my_dictionary = {
    "marks1": 55,
    "marks2": 77,
    "marks3": 88,
    "marks4": 90,
}

max_value = my_dictionary["marks1"]
max_key = "marks"
for key, value in my_dictionary.items():
    if value > max_value:
        max_value = value
        max_key = key
print(f"max key is {max_key} and max value is {max_value}")
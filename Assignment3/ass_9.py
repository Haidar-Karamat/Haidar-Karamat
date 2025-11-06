
students = {
    'names': ['Sakib', 'Ubaid', 'Adnan'],
    91: {'name': 'Haidar', 'state': 'U.P'},
    'marks': (45, 78.8, 33)
}
key = input('Enter key to check-')
found = False
for keys, values in students.items():
    if key == str(keys):
        found = True
        break

if found:
    print(f"{key} is present")
else:
    print(f"{key} not present")
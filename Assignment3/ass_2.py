
students = {
    'TCA091' : {'name' : 'Haidar', 'marks' : 70},
    'TCA138' : {'name' : 'Ubaid', 'marks' : 98},
    'TCA011' : {'name' : 'Haidar', 'marks' : 88},

}
for roll_no, info in students.items():
    print(f"{roll_no}\t{info['name']}\t{info['marks']}")
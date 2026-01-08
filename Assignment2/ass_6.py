list_of_student = ['Haidar', 'Ubaid', 'Adnan', 'Faraz', 'Hassan']
#Addition
list_of_student.append('Tomar')#append --> add item in a list in last index
list_of_student.insert(2, 'Mohit')#add element index wise

#remove
list_of_student.pop(2) #removing idex wise
list_of_student.remove('Ubaid')
del list_of_student[3]

print(list_of_student)

#Accessing

print(list_of_student[0])
for name in list_of_student:
    if name == 'Tomar':
        print(f"{name} is present")
    else:
        print(f"{name} is not present")
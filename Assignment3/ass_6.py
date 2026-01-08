
dict1 = {
    'name': ['hasi', 'fasi'],
    'sub': ['math', 'physics']
}

dict2 = {
    'marks': [44, 89],
}

result = {}

for key in dict1:
    result[key] = dict1[key]

for key in dict2:
    result[key] = dict2[key]

print(result)
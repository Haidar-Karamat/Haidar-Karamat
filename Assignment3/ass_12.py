def merge_dicts_add_values(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] += dict2[key]
        else:
            dict1[key] = dict2[key]
    return dict1

dict1 = {"Haidar": 45, "Hamza": 55}
dict2 = {"Haidar" : 90, "Ubaid": 95}
print(merge_dicts_add_values(dict1, dict2))
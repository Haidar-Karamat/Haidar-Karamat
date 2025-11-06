def lists_to_dict(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}

keys = ["name", "age", "city"]
values = ["Haidar", 20, "Moradabad"]

print(lists_to_dict(keys, values))
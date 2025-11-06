def delete_key_if_exists(my_dict, key):
    try:
        del my_dict[key]
    except KeyError:
        print(f"Key '{key}' not found. No deletion performed.")

data = {"name": "Haidar", "age": 20}
delete_key_if_exists(data, "hjj")
print(data)
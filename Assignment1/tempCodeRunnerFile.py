users = [ 
    (0, 'Bob', 'passward'),
    (1, 'marlin', 'hdjk3fh'),
    (2, 'jack', 'kjs3@j3'),
]

user_maping = {user[1]: user for user in users}

username_input = input("Enter your username-")
passward_input = input("Enter your passward-")

_, username, passward = user_maping[username_input]
if username_input != username:
    raise ValueError('User name is not found')
if passward_input == passward:
    print("your detail is correct")
else :
    print("your detail is incorrect")

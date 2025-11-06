# some_list = ['a', 'm', 'h', 'a', 'k', 'n', 'k', 'j', 'p']
#
# duplicate_element = []
#
# for val in some_list:
#    if some_list.count(val) > 1:
#        duplicate_element.append(val)
#        print(val)
#
# print(some_list[:-1])
#
#
#
# some_list = ['a', 'm', 'h', 'a', 'k', 'n', 'k', 'j', 'p']
#
# for i, element in enumerate(some_list):
#    for j, other_element in enumerate(some_list):
#        if i != j and element == other_element:
#            print(f"Duplicate element is: {element}")
#
#
# def pie():
#    return 3.14
#
# print(pie())
#
# def highest_even(lis):
#    max_even = None
#    for num in lis:
#        if num % 2 == 0:
#            if max_even is None or num > max_even:
#                max_even = num
#    return max_even
#
# out = highest_even([10, 2, 5, 8, 11, 13, 12])
# print(out)
#
##dictionary comprehension
# users = [
#    (0, 'Bob', 'passward'),
#    (1, 'marlin', 'hdjk3fh'),
#    (2, 'jack', 'kjs3@j3'),
# ]
#
# user_maping = {user[1]: user for user in users}
#
# username_input = input("Enter your username-")
# passward_input = input("Enter your passward-")
#
# if username_input not in user_maping:
#    print(f"Username {username_input} is not found. please try again")
# else:
#    _, username, passward = user_maping[username_input]
#
#    if passward_input == passward:
#        print("your detail is correct")
#    else :
#        print("your detail is incorrect")
#
# student = {'name' : 'Jose', 'school' : 'Computing', 'grades' : (66, 77, 88,)}
#
# print(student['grades'])
#
# items = []
# name = 'Haider'
# price = (12, 33, 77, 88)
# item = {'name' : name, 'price' : price}
# items.append(item)
# print(items[0]['price'])
# total = 0
# for p in items[0]['price']:
#    total += p
# print(total)


class Car:
    FUEL_TYPES = ("Electic", "Hybrid", "Fossil Fuel")

    def __init__(self, seat_capacity, company, horse_power, catagory, fuel_type):
        self.seat_capacity = seat_capacity
        self.company = company
        self.horse_power = horse_power
        self.catagory = catagory
        self.fuel_type = fuel_type

    def __repr__(self):
        return f"Brand {self.company}, {self.seat_capacity}, {self.horse_power}Hp, Type {self.catagory}, Fuel {self.fuel_type}"

    @classmethod
    def Electric(cls, no_of_motors, range, seat_capacity, company, horse_power, catagory):
        num_motors = f"{no_of_motors} motor"
        range_km = f"{range} km"
        obj = cls(seat_capacity, company, horse_power, catagory, cls.FUEL_TYPES[0])
        obj.num_motors = num_motors
        obj.range_km = range_km
        return obj

    def get_elec_car_spec(self):
        print(f"{self.num_motors} ,Range {self.range_km}")

    @classmethod
    def Hybrid(cls, battery_capacity, no_of_motors, range, seat_capacity, company, horse_power, catagory):
        battery_capacity = f"{battery_capacity}Kg/w"
        obj = cls.Electric(no_of_motors, range, seat_capacity, company, horse_power, catagory)
        obj.fuel_type = cls.FUEL_TYPES[1]
        obj.battery_capacity = battery_capacity
        return obj

    def get_hybrid_car_spec(self):
        print(f"{self.num_motors} ,Range {self.range_km},Battery {self.battery_capacity}")


if __name__ == '__main__':
    elec_car = Car.Electric(2, 370, 4, 'Tesla', 120, 'Family')
    print(elec_car)
    elec_car.get_elec_car_spec()
    hybrid_car = Car.Hybrid(80, 2, 540, 7, 'Toyata', 450, 'SUV')
    print(hybrid_car)
    hybrid_car.get_hybrid_car_spec()

ele_list = ['a', 'd', 'g', 'a', 'h', 'h']
duplicate_ele = []

for i in range(len(ele_list)):
    for j in range(i + 1, len(ele_list)):
        if ele_list[i] == ele_list[j] and ele_list[i] not in duplicate_ele:
            duplicate_ele.append(ele_list[i])

print(duplicate_ele)
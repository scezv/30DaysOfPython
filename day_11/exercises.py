def add_two_numbers(n1, n2):
    return n1+n2
print('The sum of 7 and 8 is:',add_two_numbers(7,8))

def area_of_circle(radius):
    return 3.14*radius*radius
print('The area of circle with radius 7 is: ', area_of_circle(7))

def add_all_nums(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum
print('The sum of (3,4,5,6,7,8) is: ', add_all_nums(3,4,5,6,7,8))

def convert_celsius_to_fahrenheit(temp):
    return ((temp * 9/5) + 32)
print(f'The celcius conversion of 37 °C is {convert_celsius_to_fahrenheit(37) } °F')

def check_season(month):
    if month == 'January' or month == 'February':
        return str('Autumn')
print(f"The season of February is {check_season('January')}")

def reverse_list(lst):
    revLst = []
    for i in reversed(lst):
        revLst.append(i)
    return revLst
print(reverse_list([1, 2, 3, 4, 5]))

def add_item(lst, va):
    lst.append(va)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))

def remove_item(lst, va):
    lst.remove(va)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Milk'))
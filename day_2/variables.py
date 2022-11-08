first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = f'{first_name} {last_name}'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
is_light_on = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print(f'Full name: {full_name}')
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print('Is Light on: ', is_light_on)

car, van, jeep = 'sam', 'pan', {'first':'jerry', 'second':'perry'}

print(car, van, jeep['first'])

print(type(car))

print(len(first_name))

num_one, num_two = 5,4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

first_name_input = input('Enter your first name')
last_name_input = input('Enter your last name')

print(f'{first_name_input} {last_name_input}')

radius = 30

area_of_circle = 3.14*radius*radius

circum_of_circle = 2*3.14*radius

print(area_of_circle, circum_of_circle)

def area():
   radius = float(input('Enter radius'))
   area_of_circle = 3.14*radius*radius
   print(area_of_circle)
area()
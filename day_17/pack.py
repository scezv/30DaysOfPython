def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

def pack_dict(**dic):
    for key in dic:
        print(f"{key} = {dic[key]}")
    return dic


pack_dict(player='cristiano', age=19, club='real madrid')

# Spreading in Python
list_one = [1, 2, 3]
list_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)
countries = ['Nepal', 'Finland']
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

# Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

club = ['real madrid', 'chelsea', 'arsenal']
country = ['spain', 'england', 'italy']

club_and_country = []

for c, cc in zip(club, country):
    club_and_country.append({'club':c, 'country':cc})
print(club_and_country)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)
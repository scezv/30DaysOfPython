# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to learn to drive")
# else:
#     print(f"You have to wait {18 - age} years to learn to drive")
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fadd = input("Enter a fruit: ")
# if fadd in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(fadd)
#     print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    #print('Skills exists')
    middle = int((len(person['skills']) - 1) / 2)
    print(middle)
    print(person['skills'][middle])
    if 'Python' in person['skills']:
        print('Can program in Python')
    else:
        print("Can't program in python")
    if 'Javascript' in person['skills'] or 'React' in person['skills']:
        print('Front-End')
    if 'Node' in person['skills'] or 'MongoDB' in person['skills'] or 'Python' in person['skills']:
        print('Back-End')
    if 'Node' in person['skills'] or 'MongoDB' in person['skills'] or 'React' in person['skills']:
        print('Full-Stack')

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# count = 0
# while count < 5:
#     if count == 3:
#         continue
#     print(count)
#     count = count + 1

print('Implementing break statement')

for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter: ', letter)

var = 10
while var > 0:
    print('Current variable value: ', var)
    var = var - 1
    if var == 5:
        break
print("Good bye!!!!")
print('Implementing continue statement')


for letter in 'Python':
    if letter == 'h':
        continue
    print ('Current Letter: ', letter)

var = 10
while var > 0:
    print('Current variable value: ', var)
    var = var - 1
    if var == 5:
        continue
print("Good bye!!!!")

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(f'{key}: ', value) # this way we get both keys and values printed out

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for iterator in range(0,11,3):
    print(iterator)

person = {
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
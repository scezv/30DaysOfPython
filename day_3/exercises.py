age = 21
height = 160.0
value = 1-5j

base = int(input('Enter base: '))
height = int(input('Enter height: '))
print('The area of the triangle is: ', round(0.5*base*height))

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))

print('The perimeter of the triangle is: ', (side_a+side_b+side_c))

width = int(input('Enter the length: '))
length = int(input('Enter the length: '))
print('The area is: ', length * width)
print('The perimeter is: ', 2*(length+width))

print(len('python') != len('dragon'))
print(not 'on' in 'python')
print('on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print(type(str(float(len('python')))))

print(8 % 2 == 0)
print(7 // 3 == int(2.7))
print(int(float('9.8')) == 10)

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

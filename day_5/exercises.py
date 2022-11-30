lst = list()
print(lst)

lst = ['man', 'dan','tan', 'sin', '{\'country\':\'nepal\'}']
print(lst[4])
print(len(lst))
print(lst[::2])

mixed_data_types = ['serbes sary', 19, '5\'11,', 'married', 'Koteshwor']
print(mixed_data_types)
lst.pop()
lst.append('kan')
print(lst)
print(lst[2].upper())
lst.sort(reverse=True)
print(lst)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

print(full_stack[:3:])
print(full_stack[:0:-1])
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative = [i for i in numbers if i<=0]

print(negative)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [j for sublist in list_of_lists for i in sublist for j in i]
print(flattened_list)

lst = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(lst)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

count = [[sub2[0].upper(), sub2[0].upper()[:3], sub2[1].upper()] for sub in countries for sub2 in sub]
print(count)

ct = [{'country': sub2[0].upper(), 'city': sub2[1].upper()} for sub in countries for sub2 in sub]
print(ct)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

ct = [sub2[0]+ " " +sub2[1] for sub in names for sub2 in sub]
print(ct)

slope = lambda x1,x2,y1,y2:(x2-x1)/(y2-y1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
print(slope(10,5,4,2))
print(y_intercept(10,5,4,2))
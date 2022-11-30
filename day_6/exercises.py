tpl = tuple()
print(tpl)

sisters = ('sita', 'preeti', 'anisha')
brothers = ('ram', 'shyam', 'hari')

siblings = brothers + sisters

print(siblings)

family_members = list(siblings)

family_members.append('MAN')
family_members.append('WOMAN')
print(tuple(family_members))

print('ram' in family_members)
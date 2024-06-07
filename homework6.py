print('д/з по теме СЛОВАРИ')
my_dict = {'Nina': 155, 'Anjela': 168, 'Olga': 175, 'Natali': 177}
print('Мой словарь', my_dict)

print('Значение ключа Anjela:', my_dict.get('Anjela', 'Такого ключа нет'))
print('Значение ключа Natasha:', my_dict.get('Natasha', 'Такого ключа нет'))

my_dict['Oksana'] = 152
my_dict.update({'Katya': 170, 'Luda': 162})
print('Расширенный словарь', my_dict)

n = my_dict.pop('Luda')
print('Значение удаленного ключа Ludmila:', n)

print('Мой итоговый словарь:', my_dict)

print(' ')
print("д/з по теме МНОЖЕСТВА")
my_set = {5, 'name', 8, True, 0.12, 5, 'name', 8, 0.12, True}
print('Моё множество:', my_set)
print('Первое добавление:', my_set.add('forest'), 'forest')
print('Второе добавление:', my_set.add((2, 3, 'a')), (2, 3, 'a'))
print('Удалённый элемент:', my_set.remove('name'), 'name')
print('Моё отредактированное множество:', my_set)
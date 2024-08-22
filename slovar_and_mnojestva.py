my_dict = {'nastya': 1998, 'misha': 2001}
print(my_dict)
print(my_dict['nastya'])
print(my_dict.get('s1mple'))
my_dict.update({'kolya': 2001,
                'vasya': 1998})
print(my_dict)
a = my_dict.pop('vasya')
print(a)
print(my_dict)
my_set = {1, 'string', 2.5, 1, 2.5}
print(my_set)
my_set.add(3.14)
my_set.add((1, 2))
my_set.remove(2.5)
print(my_set)

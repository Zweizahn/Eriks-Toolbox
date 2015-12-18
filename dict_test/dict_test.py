__author__ = 'Erik'

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}


def string_factory(dict_list, my_string):
    result = list()
    for my_dict in dict_list:
        print(my_dict)
        print(my_string.format(**my_dict))
        result.append(my_string.format(**my_dict))
    return result


def courses(my_dicts):
    result = []
    for value in my_dicts.values():
        for key in value:
            result.append(key)
    return result


# print(string_factory(dicts,string))
# print(stats(teachers))
print(courses(teachers))

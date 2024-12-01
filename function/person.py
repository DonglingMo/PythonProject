def build_person(first_name, last_name):
    person = {'first_name': first_name, 'last_name': last_name}
    return person
print(build_person(first_name='John', last_name='Doe'))


def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person['age'] = age
    return person
print(build_person(first_name='John', last_name='Doe', age=18))
from random import randrange
from unidecode import unidecode
import csv
import requests
import pprint

def generate_characters(number, user_attributes = []):
    list_of_characters = []

    name_pool = generate_names(number)
    print("Generated names")
    trait_pool = generate_traits(number * 3)
    print("Generated traits")
    if user_attributes:
        attribute_pool = generate_attributes(number, user_attributes)
    else:
        attribute_pool = generate_attributes(number)
    print("Generated attributes")

    for x in range(number):
        new_char = {}

        new_char['Name'] = name_pool.pop(randrange(0, len(name_pool)))

        new_char['Traits'] = []
        while len(new_char['Traits']) < 3:
            new_char['Traits'].append(trait_pool.pop(randrange(0, len(trait_pool))))

        new_char['Attributes'] = attribute_pool.pop(randrange(0, len(attribute_pool)))

        list_of_characters.append(new_char)

    return list_of_characters


def generate_names(number, region=''):
    request_string = "http://uinames.com/api/?amount={}&maxlen={}".format(number, max_len)
    if region:
        request_string += "&region={}".format(region)

    req = requests.get(request_string)
    names = req.json()

    if isinstance(names, dict):
        names = [names]

    name_list = []
    for person in names:
        full_name = unidecode("{} {}".format(person['name'], person['surname']))
        name_list.append(full_name)

    return name_list

def generate_traits(number):
    with open('traits.txt', 'r') as trait_file:
        traits = [trait.rstrip() for trait in trait_file.readlines()]

    if len(traits) < number:
        raise RuntimeError("Too few traits given in file")

    trait_list = []
    while len(trait_list) < number:
        rand_int = randrange(0, len(traits))
        if traits[rand_int] not in trait_list:
            trait_list.append(traits[rand_int])
    return trait_list

def generate_attributes(number, attributes=['Strength', 'Constitution', 'Dexterity', 'Intelligence', 'Wisdom', 'Charisma']):
    attribute_sets = []
    for x in range(number):
        attribute_descriptions = []
        for attribute in attributes:
            total = 0
            for x in range(2):
                total += randrange(1, 7)
            if total < 2:
                attribute_descriptions.append("{} pathetically low".format(attribute))
            elif total >=2 and total < 7:
                attribute_descriptions.append("{} lower than average".format(attribute))
            elif total >=7 and total < 10:
                attribute_descriptions.append("{} about average".format(attribute))
            elif total >=10 and total < 12:
                attribute_descriptions.append("{} better than average".format(attribute))
            else:
                attribute_descriptions.append("{} exceptionally high".format(attribute))
        attribute_sets.append(attribute_descriptions)

    return attribute_sets

field_delimiter = ','
text_delimiter = '\"'
max_len=20

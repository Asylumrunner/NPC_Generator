from random import randrange
from unidecode import unidecode
import csv
import requests
import pprint
import re

def generate_names(number, region=''):
    request_string = "http://uinames.com/api/?amount={}&maxlen={}".format(number, max_len)
    if region:
        request_string += "&region={}".format(region)

    req = requests.get(request_string)
    names = req.json()

    name_list = []
    for person in names:
        full_name = unidecode("{} {}".format(person['name'], person['surname']))
        name_list.append(full_name)

    return name_list

field_delimiter = ','
text_delimiter = '\"'
max_len=20

pp = pprint.PrettyPrinter()
pp.pprint(generate_names(100))

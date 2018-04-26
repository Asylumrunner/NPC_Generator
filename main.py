from generator import generate_characters
from cardmaker_exporter import export
import pprint

print("Welcome to the NPC Generator")
num_chars = int(input("How many characters do you want to generate: "))

print("Do you want to use default attributes, or supply your own?")
print("1. Use the defaults (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)")
print("2. Supply my own attributes")
choice_atts = int(input("What is your selection: "))

user_supplied_attributes = []

if choice_atts == 2:
    input_att = ""
    while input_att != "QUIT":
        input_att = input("Please enter the name of an attribute, or QUIT to proceed: ")
        if input_att != "QUIT":
            user_supplied_attributes.append(input_att)

finalized = False
pp = pprint.PrettyPrinter()

while not finalized:
    characters = generate_characters(num_chars, user_supplied_attributes)
    pp.pprint(characters)
    print("Are you happy with these results?")
    print("1. Yeah, I'm happy with these")
    print("2. No, I want to reroll them")
    choice_fin = int(input("Please enter your choice: "))

    if choice_fin == 1:
        finalized = True

for character in characters:
    traits = character.pop('Traits')
    for x in range(len(traits)):
        character['Trait_{}'.format(x)] = traits[x]
    attributes = character.pop('Attributes')
    for y in range(len(attributes)):
        character['Attribute_{}'.format(y)] = attributes[y]

export(characters)

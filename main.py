from generator import generate_characters
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

characters = generate_characters(num_chars, user_supplied_attributes)
pp = pprint.PrettyPrinter()
pp.pprint(characters)

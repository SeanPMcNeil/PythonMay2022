from random import randint # from "library" import "function/class"

# def roll_dice():
#     return randint(1, 20)

# print(roll_dice())


def roll_dice(number = 1, sides = 20): # sets default parameters to run if the function is not provided any
    result = 0

    for i in range(0, number):
        result += randint(1, sides)
    
    return result

# print(roll_dice()) # call w/ default parameters
# print(roll_dice(1, 20)) # can still call a single 20 sided die (or any other amounts)
# print(roll_dice(3, 6)) # changing both defaults
# print(roll_dice(number = 2)) # change change either argument individually

def generate_new_character():
    # rolls six sets of 3d6 dice and supplies them as stats
    # in dictionary format
    character = {}

    character['STR'] = roll_dice(3, 6)
    character['DEX'] = roll_dice(3, 6)
    character['CON'] = roll_dice(3, 6)
    character['WIS'] = roll_dice(3, 6)
    character['INT'] = roll_dice(3, 6)
    character['CHA'] = roll_dice(3, 6)

    return character

def generate_new_character2():

    character = {}
    stats = ['STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']

    for stat in stats:
        character[stat] = roll_dice(3, 6)

    return character

def generate_new_character3():

    character = {
        'STR': roll_dice(3, 6),
        'DEX': roll_dice(3, 6),
        'CON': roll_dice(3, 6),
        'WIS': roll_dice(3, 6),
        'INT': roll_dice(3, 6),
        'CHA': roll_dice(3, 6)
    }

    return character

new_character = generate_new_character()
print(new_character)

new_character2 = generate_new_character2()
print(new_character2)

new_character3 = generate_new_character3()
print(new_character3)
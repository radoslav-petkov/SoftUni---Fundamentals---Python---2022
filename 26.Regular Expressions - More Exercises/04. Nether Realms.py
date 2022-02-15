
import re

def calc_health(demon_name):
    health_ascii = re.compile(r'[^\d\+\-\/\*\.]')

    healt_match = health_ascii.findall(demon_name)
    demon_health = sum([ord(x) for x in healt_match])
    return demon_health

def calc_damage(demon_name):
    base_damage = re.compile(r'((?:-)?\d+(?:\.\d*)?)')
    damage_multiplier = re.compile(r'[\*\/]')

    damage_match = base_damage.findall(demon_name)
    demon_damage = sum([float(x) for x in damage_match])

    multiplier_match = damage_multiplier.findall(demon_name)
    for match in multiplier_match:
        if match == '*':
            demon_damage *= 2
        elif match == '/':
            demon_damage /= 2

    return demon_damage

input_names = input()
names_capture = re.compile(r'([^,\s]+)')
demon_names = names_capture.findall(input_names)
demon_names.sort()

for name in demon_names:
    health = calc_health(name)
    damage = calc_damage(name)
    print(f'{name} - {health} health, {damage:.2f} damage')



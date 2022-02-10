import re

message_parser = re.compile(r'(?<=@)([a-zA-Z]+)(?:[^\@\!\:\>\-]+)?(?::(\d+))(?:[^\@\!\:\>\-]+)?!(A|D)!(?:[^\@\!\:\>\-]+)?->(\d+)')

def decrypt(message):
    decrypt_symbols = r'[starSTAR]'
    decrypt_matches = re.findall(decrypt_symbols, message)
    key = len(decrypt_matches)
    return ''.join([chr(ord(x) - key) for x in message])

planets_attacked = []
planets_destroyed = []

number_of_messages = int(input())

for _ in range(number_of_messages):
    encrypted_message = input()
    decrypted_message = decrypt(encrypted_message)

    parsed_message = message_parser.search(decrypted_message)
    if parsed_message:
        attack_result = parsed_message.group(3)
        planet_name = parsed_message.group(1)
        if attack_result == 'A':
            planets_attacked.append(planet_name)
        elif attack_result == 'D':
            planets_destroyed.append(planet_name)

planet_count = len(planets_attacked)
print(f'Attacked planets: {planet_count}')
if planet_count > 0:
    planets_attacked.sort()
    for planet in planets_attacked:
        print(f'-> {planet}')

planet_count = len(planets_destroyed)
print(f'Destroyed planets: {planet_count}')
if planet_count > 0:
    planets_destroyed.sort()
    for planet in planets_destroyed:
        print(f'-> {planet}')
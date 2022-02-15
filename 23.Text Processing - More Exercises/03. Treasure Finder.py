key = ''.join([x for x in input().split(' ')])

while True:
    encrypted_coordinates = input()
    if encrypted_coordinates == 'find':
        break

    while len(key) < len(encrypted_coordinates):
        key += key

    decrypted_coordinates = ''
    for i in range(len(encrypted_coordinates)):
        decrypted_coordinates += chr(ord(encrypted_coordinates[i]) - int(key[i]))

    treasure = decrypted_coordinates[decrypted_coordinates.find('&') + 1:]
    treasure = treasure[:treasure.find('&')]
    coordinates = decrypted_coordinates[decrypted_coordinates.find('<') + 1:decrypted_coordinates.find('>')]

    print(f'Found {treasure} at {coordinates}')
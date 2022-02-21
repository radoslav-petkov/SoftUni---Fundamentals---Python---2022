data = input()

apartments = {}

while not data == 'collectApartments':
    splitted_data = data.split(' -> ')
    neighborhood = splitted_data[0]
    block_numbers_list_str = splitted_data[1].split(',')
    block_numbers_list = list(map(int, block_numbers_list_str))

    if not neighborhood in apartments.keys():
        apartments[neighborhood] = {}
        for number in block_numbers_list:
            apartments[neighborhood][number] = {'available_apartments': 0, 'price_for_apartment': None}

    else:
        for number in block_numbers_list:
            if not number in apartments[neighborhood].keys():
                apartments[neighborhood][number] = {'available_apartments': 0, 'price_for_apartment': None}

    data = input()

data = input()

while not data == 'report':
    splitted_data = data.split(' -> ')
    neighborhood = splitted_data[0].split('&')[0]
    block_number = int(splitted_data[0].split('&')[1])
    available_apartments_count = splitted_data[1].split('|')[0]
    price_per_apartment = splitted_data[1].split('|')[1]

    if neighborhood in apartments.keys():
        if block_number in apartments[neighborhood].keys():
            apartments[neighborhood][block_number]['available_apartments'] = available_apartments_count
            apartments[neighborhood][block_number]['price_for_apartment'] = price_per_apartment

    data = input()


ordered_apartments = sorted(apartments.keys())
for neighborhood in ordered_apartments:
    print(f'Neighborhood: {neighborhood}')
    ordered_block_numbers = sorted(apartments[neighborhood].keys())
    for number in ordered_block_numbers:
        print(f"* Block number: {number} -> {apartments[neighborhood][number]['available_apartments']} apartments for sale. Price for one: {apartments[neighborhood][number]['price_for_apartment']}")

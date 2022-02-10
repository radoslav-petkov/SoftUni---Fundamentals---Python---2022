class Party:
    def __init__(self) -> None:
        self.people = []
        pass

party = Party()

while True:
    input_data = input()
    if input_data == 'End':
        break

    party.people.append(input_data)

print(f'Going: '+ ', '.join(party.people))
print(f'Total: {len(party.people)}')
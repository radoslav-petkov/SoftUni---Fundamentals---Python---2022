def mutate_data(data_type,data):
    if data_type == 'int':
        output = int(data) * 2
    elif data_type == 'real':
        output = float(data) * 1.5
        output = '{:.2f}'.format(output)
    elif data_type == 'string':
        output = '$' + data + '$'

    return output


output = mutate_data(input(),input())
print(output)
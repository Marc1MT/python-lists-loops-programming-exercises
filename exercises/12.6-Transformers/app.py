incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:
def data_transformer(data):
    # Define a lambda function to format the full name
    format_full_name = lambda person: f"{person['name']} {person['last_name']}"

# Use map to apply the format_full_name function to each person's data
    full_names = list(map(format_full_name, data))

    return full_names

print(data_transformer(incoming_ajax_data))
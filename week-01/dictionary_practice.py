phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print phonebook_dict['Alice']
phonebook_dict['Kareem'] = '938-489-1234'
phonebook_dict.pop('Alice')
phonebook_dict['Bob'] = '968-345-2345'
phonebook_length = len(phonebook_dict)
for first_name in phonebook_dict:
    print phonebook_dict[first_name]
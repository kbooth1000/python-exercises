string = raw_input('Text to encrypt/decrypt: ')
displacer = int(raw_input('Displacement value: '))
string_list = list(string)
string_length = len(string_list)
alph_list = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alph_list_length = len(alph_list)
displaced = 0
for i in range(0, string_length):
    string_list[i] = string_list[i].upper()
    for j in range(0, alph_list_length):
        
        if string_list[i] == alph_list[j]:
            displaced = j + displacer
            if displaced > alph_list_length - 1:
                displaced = displaced - alph_list_length + 1
            elif displaced < 1:
                displaced = alph_list_length + displaced - 1
        elif string_list[i] == ' ':
            displaced = 0

    string_list[i] = alph_list[displaced]

print
print ''.join(string_list)
print
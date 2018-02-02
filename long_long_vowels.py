string = raw_input('A word: ')
string_list = list(string)
string_length = len(string_list)

for i in range(1, string_length):
    if (string_list[i] == 'a' or string_list[i] == 'e'  or string_list[i] == 'o') and string_list[i] == string_list[i-1]:
        string_list[i] = (string_list[i] * 4)

print ''.join(string_list)
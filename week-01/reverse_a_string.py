string = raw_input('A string for me to Leet, please: ')
string_length = len(string)
string_leet = ''
leet = []
leet_chars = [A,E,G,I,O,S,T]
leet_nums = [4,3,6,1,0,5,7]

for i in range(0, string_length-1):
    for j in range(0, len(leet_chars)):
        if string[i] == leet_char[j]:
        string[i] = leet_num[j]
    string_leet = string_leet + leet[i]

print string_leet[::-1] #reverse the string

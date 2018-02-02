string = raw_input('A string for me to Leet, please: ')
string_list = list(string)
string_length = len(string)
leet_chars = ['A','E','G','I','O','S','T','B']
leet_nums = ['4','3','6','1','0','5','7','8']

for i in range(0, string_length):
    string_list[i] = string_list[i].upper()
    for j in range(0, len(leet_chars)):
        if string_list[i] == leet_chars[j]:
            string_list[i] = leet_nums[j]
            break

print ''.join(string_list)
text_to_analyze = raw_input('Text to analyze: ')
letter_histogram = {}
letter_list = list(text_to_analyze)

for letter in letter_list:
    letter_histogram[letter] = letter_list.count(letter)

print letter_histogram
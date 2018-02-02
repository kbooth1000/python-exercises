text_to_analyze = raw_input('\nText to analyze: ')
word_histogram = {}
letter_list = list(text_to_analyze)
letter_list_length = len(letter_list)
words = []
separator_prev = -1
word_index = 0

#get words from list of letters
for i in range(0, letter_list_length):
    
    if letter_list[i] == ' ' or i >= letter_list_length:

        words.append(''.join(letter_list[separator_prev+1: i]))
        separator_prev = i
        print words[word_index]
        word_index += 1

#iterate through words in list "words" and count occurrences of each
for i in range(0, len(words)):
    word_to_add = words.count(words[i])
    word_histogram[words[i]] = word_to_add
print word_histogram
text_to_analyze = raw_input('\nText to analyze: ')
word_histogram = {}
words = []

#get words from list of letters
words = text_to_analyze.split()

#iterate through words in list "words" and count occurrences of each
for i in range(0, len(words)):
    word_to_add = words.count(words[i])
    word_histogram[words[i]] = word_to_add
print word_histogram
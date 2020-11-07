with open('words.txt', 'r') as fd:
    wordList = fd.read().split()

print [word for word in wordList if len(word) > 20]

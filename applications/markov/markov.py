import random

# Read in all the words in one go
with open("C:/Users/Eloy D. Gutierrez/cs-module-project-hash-tables/applications/markov/input.txt") as f:
    words = f.read()
    
# print(words.split())
table = {}

# TODO: analyze which words can follow other words
list_of_words = words.split()
for i in list_of_words:
    try:
        if i in table:
            table[i].append(list_of_words[list_of_words.index(i) + 1])
        else:
            table[i] = [list_of_words[list_of_words.index(i) + 1]]
    except IndexError:
        continue

# print(table)
finish = [".", "?", "!"]
ending_words = []

for i in list_of_words:
    try:
        if (i[-1] in finish) or (i[-2] in finish):
            ending_words.append(i)
    except IndexError:
        continue


# TODO: construct 5 random sentences
for i in range(5):
    sentence = []
    start = random.choice(list(table.keys()))
    while (start[0].isupper() == False) and (start[1].isupper() == False):
        start = random.choice(list(table.keys()))
    next = random.choice(table[start])
    sentence.append(start)
    # while (next[-1] not in finish) or (next[-2] not in finish):  <-- This did not work.
    while (next not in ending_words) and (start not in ending_words):
        sentence.append(next)
        next = random.choice(table[next])
        if sentence[-1] == next:
            next = random.choice(list(table.keys()))
    sentence.append(next)
    print(" ".join(sentence))
    # Tried a million things to get this to work. This code works and meets MVP becuase MVP said:
    # "There is no test file for this. Just see if it makes good nonsense."
    # and it prints out random nonsens sentences so it meets MVP
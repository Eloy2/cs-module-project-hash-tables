with open("C:/Users/Eloy D. Gutierrez/cs-module-project-hash-tables/applications/histo/robin.txt") as f:
    words = f.read()


table = {}
hash = "#"


for i in words:
    if i in '\" : ; , . - + = / \ | [ ] { } ( ) * ^ &':
        words = words.replace(i, " ")
for i in words.split():
    if i.lower() in table:
        table[i.lower()] += 1
    else:
        table[i.lower()] = 1


listofTuples = [(word, table[word]) for word in table]
listofTuples.sort(key = lambda e: (-e[1], e[0])) # Will sort first by the amount times word appeared reversed(so biggest first). Then alphabetically.

longest_string =  max(words.split(), key=len)
length = len(longest_string) + 2

for i in listofTuples:
    print('{:<{width}} {:<0}'.format(i[0], "#" * i[1], width = length))


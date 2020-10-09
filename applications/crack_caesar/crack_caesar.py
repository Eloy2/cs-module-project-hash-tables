# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
table = {}
decode_table = {}
check_list = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("C:/Users/Eloy D. Gutierrez/cs-module-project-hash-tables/applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()

for i in words:
    if i not in check_list:
        continue
    if i in table:
        table[i] += 1
    else:
        table[i] = 1

listofTuples = sorted(table.items() ,  reverse = True, key=lambda x: x[1])

index = 0

for i in listofTuples:
    decode_table[i[0]] = check_list[index]
    index += 1

final = ""

for i in words:
    if i not in check_list:
        final += i
        continue
    final += decode_table[i]

print(final)

print(listofTuples)
print()
print(decode_table)
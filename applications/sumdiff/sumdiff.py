"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
print("Brute Force with duplicates")
for a in q:
    for b in q:
        for c in q:
            for d in q:
                if (f(a) + f(b)) == (f(c) - f(d)):
                    print(f'f({a}) + f({b}) = f({c}) - f({d})  {f(a)} + {f(b)} = {f(c)} - {f(d)}')

print()
print("Hash Table version without duplicates")
sum_table = {}
sub_table = {}

for num1 in q:
    for num2 in q:
        x = f(num1) + f(num2)
        y = f(num1) - f(num2)
        sum_table[x] = (num1, num2)
        sub_table[y] = (num1, num2)

for k,v in sum_table.items():
    for c,b in sub_table.items():
        if k == c:
            print(f'f({v[0]}) + f({v[1]}) = f({b[0]}) - f({b[1]})  {f(v[0])} + {f(v[1])} = {f(b[0])} - {f(b[1])}')


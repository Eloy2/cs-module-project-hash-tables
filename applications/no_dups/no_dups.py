def no_dups(s):
    table = {}
    final = []
    for i in s.split(" "):
        if i not in table:
            table[i] = i
            final.append(i)
    separator = " "
    return separator.join(final)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
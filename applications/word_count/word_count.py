def word_count(s):
    table = {}

    for i in s:
        if i in "\" : ; , . - + = / \ | [ ] { } ( ) * ^ &":
            s = s.replace(i, " ")
    for i in s.split():
        if i.lower() in table:
            table[i.lower()] += 1
        else:
            table[i.lower()] = 1

    return table



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
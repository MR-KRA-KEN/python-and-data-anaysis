def word(s):
    d={}
    for char in s:
        d[char]=s.count(char)
    return d

print(word('nishchal bhuria'))
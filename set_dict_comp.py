square={i:i**2 for i in range(1,11)}
print(square)

string='nishchal bhuria'
new={char:string.count(char) for char in string}
print(new)

odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

s={k*2 for k in range(1,11)}
print(s)
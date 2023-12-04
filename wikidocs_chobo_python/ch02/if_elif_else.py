a = 1234 * 4 
b = 13456 / 2
if a > b:
    print('a')
else:
    print('b')            


c = 15 * 5
d = 15 + 15 + 15 + 15 + 15
if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else: 
    print('I don\'t know')

a = 48
b = 4
if a % b == 0:
    print(f'{a} is divided by {b} perfectly.')
elif a % b != 0:
    print(f'{a} is not devided by {b} perfectly.')
    
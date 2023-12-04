print('Right triangle\n')
leg = int(input('leg: '))

for i in range(leg):
    print('*' * (i+1))

area = (leg ** 2 )/2
print('Area: ', area)

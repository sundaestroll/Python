bounce = 1
height = 100
h = height *(3/5)
while bounce <= 10:
    h = height *(3/5)
    print(bounce,h)
    bounce +=1
    height = h

bounce = 1
height = 100
h = height *(3/5)
while bounce <= 10:
    h = height *(3/5)
    print(bounce,round(h,4))
    bounce +=1
    height = h

#answer from the author
height = 100
bounce = 3/5

i = 1

while i <= 10:
    height = height * bounce
    print(i,round(height,4))
    i = i + 1
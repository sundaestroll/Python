year = int(input('What year were your born? '))
if year <= 1924:
    print("You're the Greatest Generation.")
elif year <= 1945:
    print("You're the Silent Generation.") 
elif year <= 1964:
    print("You're a baby boomer.") 
elif year <= 1980:
    print("You're a Generation X.") 
elif year <= 1996:
    print("You're a millennial.") 
elif year >= 1997:
    print("You're a Generation Z.") 

#Answer from the author

y = int(input('What year were you born? '))

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945:
    gen = 'the Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")
for x in [1,2,3,4]:
    print(x)
else:
    print("all the elements from the list are posted.")
# 위의 코드만 보면, 마지막 출력을 굳이 else 블록에 넣지 않고 반복문 바깥에 두어도 될 것 같죠? 하지만 아래처럼 break가 등장하면 얘기가 달라집
for x in[1,2,3,4] :
    if x % 3 :
        print(x)
    else: 
        break
else: 
    print("all the elements from the list are posted.")
# 여기서는 반복문을 break했는데, 그럴 때는 else 블록이 실행되지 않습니다.

countdown = 5
while countdown >0:
    print(countdown)
    countdown -= 1
    if input() == 'stop':
        break
    else:
        print('go')
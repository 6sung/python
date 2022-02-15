'''
while 조건식:
    종속문장
'''
i=0
while i<5:
    print(i, "종속문장")
    i += 1
print("다음 문장들 실행")
#for문으로 변경해 주세요~

for i in range(5):
    print(i, "종속문장")
print("다음 문장들 실행")

i=1
odd, even = 0,0
while i<=10:
    if i%2 == 0:
        even+=i
    else:
        odd += i
    i += 1
print("1-10 짝수의 합 : ",even)
print("1-10 홀수의 합 : ",odd)

#for 문으로 변경해 주세요

odd, even = 0,0
for i in range(1,11,1):
    if i%2 == 0:
        even+=i
    else:
        odd += i
print("for,1-10 짝수의 합 : ",even)
print("for,1-10 홀수의 합 : ",odd)

i=0
while i<5:
    print(i,'종속문장')
    i += 1
else:
    print('어떨때 실행??? i : ',i)
print("다음 문장들 실행")

i=0
flag = True
while flag:
    print('aaaa')
    if i == 3:
        flag = False
    i += 1
'''
제어문 : 프로그램의 흐름을 제어한다.
if, for, while, break, continue
break
    - 반복문 안에서만 사용할 수 있다.
    - break를 만나면 반복문을 바로 빠져나온다.
continue
    - 반복문에서만 사용한다.
    - continue를 만나면 반복문의 위로 이동시킨다.
'''
i = 0
while True:
    if i==3:
        print('33333')
        break
    print(i,'출력')
    i+=1
print('다음 문장')

i=0
while i<5:
    i+=1
    if i == 3:
        continue
    print(i,'출력')
print('다음문장실행!!!')


for i in range(1,6):
    if i == 3:
        continue
    print(i,'출력')
print('다음문장실행!!!')















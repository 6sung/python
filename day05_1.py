'''
규칙적으로 값이 변한다면 반복문 사용
'''
'''
# (i=1;i<11;i++)
for i in range(1,11,1): #range(시작값, 비교값, 증가값)
    print(i)

sum_=0
num=1
for num in range(1,11,1):
    sum_+=num
print(sum_)


for num in range(0,11,2):
    print(num, end=" ")
print("\n")

'''
'''
1 2 3 4 5
6 7 8 9 10
11 .... 30

'''
'''
sum_=0
for i in range(1,7,1):
    for j in range(1,6,1):
        sum_+=1
        print(sum_,end="  ")
    print("\n")

#수를 입력받아 1~n까지 합 구하세요
num = int(input("수를 입력하세요 : "))
sum_=0
for i in range(1,num+1,1):
    sum_+=i
print("1부터 n까지의 총 합 : ",sum_)    

#수를 입력 받아 1~n까지 짝,홀, 총합을 구하세요
num = int(input("수를 입력하세요 : "))
sum_=0
sum1=0
sum2=0
for i in range(1,num+1,1):
    sum_+=i
    if i%2==0:
        sum1+=i
    else :
        sum2+=i
print("1부터 n까지의 총 합 : ",sum_)
print("1부터 n까지의 짝수 총 합 : ",sum1)
print("1부터 n까지의 홀수 총 합 : ",sum2)

'''
'''
'''

for i in range(1,10):
    print(i,end=" ")
print("\n")
for i in range(10):
    print(i,end=" ")

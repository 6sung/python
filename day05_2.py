#1~100 사이의 값 중 3의 배수이면서 5의배수 아닌 수 합

sum_=0
for i in range(1,101,1):
    if i%3==0 and i%5!=0:
        pass
    else :
        sum_+=i
print("총 합 : ",sum_)

'''
# 두 수를 입력받아 입력 받은 사이의 합을 구하세요
'''
'''
num1 = int(input("첫 번째 수를 입력 하세요"))
num2 = int(input("두 번째 수를 입력 하세요"))
tmp = 0
sum_=0
if num1>num2:
    tmp=num1
    num1=num2
    num2=tmp
for i in range(num1,num2+1,1):
    sum_+=i
print(num1,"과",num2,"사이 수의 총 합은 ",sum_,"입니다.")
'''

#첫날에 10원예금, 다음날 전날 2배 예금, 한달(30일)동안 저축한 금액 구하시오
'''
sum_=0
cnt=10
for i in range(1,31,1):
    sum_+=cnt
    cnt*=2
print("30일째 입금 금액 : ",int(cnt/2))
print("30일 동안 저축 총 금액 : ",sum_)
'''


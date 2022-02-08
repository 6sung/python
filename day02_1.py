'''
결과 : num1(10) + num2(20) = 30
'''

num1=10
num2=20
sum_=num1+num2

print("결과 : num1(",num1,") + num2(",num2,") = ",sum_)

'''변수에 수 저장후 +,-,*,/ 연산
단, 연산 결과 값은 변수에 저장하여 출력 하세요
'''

num1=10
num2=3
result=0
result = num1+num2
print("결과 : num1(",num1,") + num2(",num2,") = ",result)
result = num1-num2
print("결과 : num1(",num1,") - num2(",num2,") = ",result)
result = num1*num2
print("결과 : num1(",num1,") * num2(",num2,") = ",result)
result = num1/num2
print("결과 : num1(",num1,") / num2(",num2,") = ",result)

print('round : ',round(result,2))

'''
3과목 합과 평균을 구하세요(평균은 소수점 2자리)
'''
sbj1=100
sbj2=95
sbj3=70
result=sbj1+sbj2+sbj3
print("\n\n3과목 합 : ",result)
result=result/3
print("3과목 평균 : ",round(result,2))


'''
당신은 놀이공원을 가기 위해 11개의 지하철 역을 지나왔다. 출발 역에서 도착역까지
37분이 걸렸다면 한 역을 지나는데 걸리는 시간은 얼마인가?(소수점 2자리 까지 출력)
'''

station=11
minute=37
result=minute/station
print("\n\n한 역을 지나는데 걸리는 시간 : ",round(result,2))


'''
호텔 한 층의 높이는 260cm이다. 총 14개의 층을 쓰고 있으며 1층은 500.23cm이라면
이 건물의 높이는 총 몇 m인가 (소수점 3자리까지)
'''

height=260
floor=14
floor_1=500.23
result=260*(floor-1)+floor_1
result=result/100
print("\n\n건물의 총 높이 : ",round(result,3),"m")



num=100
print("\nnum : ",type(num))

num=100.111
print("\nnum : ",type(num))

num='100.111'
print("\nnum : ",type(num))

st1='python'
st2='test'
su=100
flt=1.111
num='100'

print(st1+st2)
print(su+flt)

print(su+int(num))

'''
아래와 같이 출력 하시오.
각각의 값들은 하나씩만 사용할 것
200
101.111
100100
'''
print(su+int(num))
print(float(num)+flt)
print(num+str(su))

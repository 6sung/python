'''
if 조건식:
    종속문장
elif 조건식:
    종속문장
elif 조건식:
    종속문장
'''
'''
num = int(input("수 입력 : "))
if num > 100:
    print("100보다 크다")
elif num > 90:
    print("90보다 크다")
elif num > 80:
    print("80보다 크다")
else:
    print("그 외의 값")
'''

'''
name = input("이름을 입력하세요. ")
studentnb = input("학번을 입력하세요. ")
print("세과목 점수를 입력하세요.")
score1=int(input())
score2=int(input())
score3=int(input())
sum_=score1+score2+score3
avg=sum_/3
if avg>90:
    grade="A"
elif avg>80:
    grade="B"
elif avg>70:
    grade="C"
elif avg>60:
    grade="D"
else:
    grade = "F"
print("이름    학번  국 영 수합 평균   등급")
print(name,"",studentnb," ",score1,score2,score3,sum_,round(avg,2),grade)
'''

'''
num=int(input("커피의 개수를 입력하세요."))
if num>10:
    sum_=1500*(num-10)+20000
else:
    sum_=num*2000
print("커피의 총 금액은",sum_,"원 입니다.")
'''
'''
num = int(input("정수를 입력하세요. "))
if num==0:
    print("0은 3의 배수도 4의 배수도 아닙니다.")
elif num%3==0:
    if num%4==0:
        print("3의 배수이면서 4의 배수입니다.")
    else:
        print("3의 배수입니다.")
elif num%4==0:
    print("4의 배수 입니다.")
else:
    print("3의배수도 4의배수도 아닙니다.")
'''
num = int(input("비행기 탑승 시간을 입력하세요."))
if num <= 30:
    sum_=30000
else:
    sum_=int((num-20)/10)*5000 + 30000
print("총 요금은 ",sum_,"원 입니다.")

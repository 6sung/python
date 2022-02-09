'''
name = input("학생 이름 : ")
sbj1 = int(input("국어 점수 : "))
sbj2 = int(input("영어 점수 : "))
sbj3 = int(input("수학 점수 : "))
sum_ = sbj1+sbj2+sbj3
avg = sum_/3
print("======================학생 정보======================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print(name,"",sbj1,"\t",sbj2,"\t",sbj3,"\t",sum_,"\t",round(avg,2))
'''

print('안녕하세요 안녕하세요 안녕하세요\
      안녕하세요 안녕하세요')

n1=9; n2=2;
print('n1 + n2 =',n1+n2)
print('n1 - n2 =',n1-n2)
print('n1 * n2 =',n1*n2)
print('n1 / n2 =',n1/n2)
print('n1 // n2 =',n1//n2) #몫
print('n1 % n2 =',n1%n2) #나머지
print('n1 ** n2 =',n1**n2) #제곱

su1 = 3; su2 = 4;
print(su1 > su2)
print(su1 <= su2)
print(su1 == su2)
print(su1 != su2)
print('----------------------')

su1= su2=5
su1+=1
print("su1 + 1 = ",su1)
su1 -= 1
print("su1 - 1 = ",su1)
su1 *= su2
print("su1 * su2 = ",su1)
su1 //= su2
print("su1 // su2 = ",su1)
su1 %= su2
print("su1 % su2 = ",su1)

print("------------------------")
su1 = 5
su2 = 3
su1 **= su2
su1 -= 2
print(su1/4)
print(su1 //4)
print(su1 % 4)
print("-----------------------")

'''
논리연산자 : 결과적으로 참 또는 거짓을 표현
-and : 모두가 참일때 참
-or : 하나라도 참이면 참
-not : 반전시켜준다. not True => False
'''

print("======or=======")
print(False or False)
print(True or False)
print(False or True)
print(True or True)

print("======and=======")
print(False and False)
print(True and False)
print(False and True)
print(True and True,"\n\n")

a=10
print(a%2==0 and a<=10)

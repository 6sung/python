# 입력한 데이터가 3의 배수인 경우 출력하시오
num = int(input("숫자를 입력하세요 : "))
num_ = num%3
if num_ == 0:
    print(num,"은 3의 배수 입니다.")
else :
    print(num,"은 3의 배수가 아닙니다.\n")

# 절대값을 구하는 프로그램을 작성하시오.
num = int(input("숫자를 입력하세요 : "))
num_ = -1
if num<0:
    num_*=num
else:
    num_=num
print(num,"의 절대값은",num_,"입니다.\n")

#수를 입력 받아 짝, 홀수를 구분하여 출력하시오.
num = int(input("숫자를 입력하세요 : "))
if num%2==0:
    print(num,"은 짝수 입니다.\n")
else :
    print(num,"은 홀수 입니다.\n")

#두수를 입력 받아 큰 수를 출력하시오.
num = int(input("첫번째 숫자를 입력하세요 : "))
num_ = int(input("두번째 숫자를 입력하세요 : "))
if num>num_:
    max_ = num
if num<num_:
    max_ = num_
print(num,"과",num_,"중에서 큰 수는 ",max_,"입니다.\n")

#세수를 입력 받아 큰 수를 출력하시오.
num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))
num3 = int(input("세번째 숫자를 입력하세요 : "))
if num1>num2:
    max_ = num1
if num1<num2:
    max_ = num2
if max_<num3:
    max_ = num3
print(num1,"과",num2,"과",num3,"중에서 큰 수는 ",max_,"입니다.\n")

#두수를 입력 받아 큰 수가 짝수이면 출력하시오.
num = int(input("첫번째 숫자를 입력하세요 : "))
num_ = int(input("두번째 숫자를 입력하세요 : "))
if num>num_:
    max_ = num
if num<num_:
    max_ = num_

if max_%2==0:
    print("큰 수인",max_,"는 짝수입니다.\n")
else:
    print("큰 수인",max_,"는 짝수가 아닙니다.\n")

#두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.
num = int(input("첫번째 숫자를 입력하세요 : "))
num_ = int(input("두번째 숫자를 입력하세요 : "))
if num%2==0 and num%3==0:
    print(num,"은 짝수이고 3의 배수입니다.")
if num_%2==0 and num_%3==0:
    print(num_,"은 짝수이고 3의 배수입니다.")
else:
    print(num,"과",num_,"은 짝수 및 3의 배수가 아닙니다.")

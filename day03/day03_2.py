'''
제어문
-프로그램의 흐름을 제어
if, for, while, break, continue..
'''

'''
print('1. 쉬운게임')
print('2. 어려운게임')
print('3. 종료')
num = int(input('>>> : '))
if num == 1 :
    print("쉬운 게임 실행")
if num == 2 :
    print("어려운 게임 실행")
if num == 3 :
    print("프로그램 종료")
'''
'''
num1=10
num2=50
if num1>num2:
    print("num1이 num2보다 크다")
print("다음 문장들 실행")

num1 = int(input("수 입력 : "))
if num1 % 2 ==0:
    print("입력한 수는 짝수 입니다. ",num1)
    print("입력한 수는 2의 배수 입니다. ",num1)
if num1 % 2 != 0:
    print("입력한 수는 홀수 입니다. ",num1)
print("다음 문장들 실행")

'''
'''
날짜를 입력받아 요일을 구하세요
1일은 무조건 월요일, 7일은 일요일
'''

day = int(input("날짜를 입력하세요 : "))
day_ = day%7
if day_ == 0:
    print(day,"일은 일요일입니다.")
if day_ == 1:
    print(day,"일은 월요일입니다.")
if day_ == 2:
    print(day,"일은 화요일입니다.")
if day_ == 3:
    print(day,"일은 수요일입니다.")
if day_ == 4:
    print(day,"일은 목요일입니다.")
if day_ == 5:
    print(day,"일은 금요일입니다.")
if day_ == 6:
    print(day,"일은 토요일입니다.")

'''
    if 조건식 :
        종속문장
    else :
        종속문장
if 조건식이 참이면 if의 종속문장이 실행
만약 거짓이면 else의 종속문장이 실행
결과적으로 둘중 하나만 실행된다.
'''
'''
num = int(input("수 입력 : "))
if num==1 :
    print("1 입력")
else:
    print("1이외의 수 입력")
print("다음 문장들 실행!")
'''
'''
arr= [10,20,30,40]
print(10 in arr)

st = "Hello Python Fun!!!"
na = input("찾고자하는 값 입력 : ")
if na in st:
    print("st : ",st,"찾는 문자열 : ",na,"존재함.")
else:
    print(st,"찾는 문자열 없음.",na)
print("다음 문장들 실행!")
'''
'''
saveId = input("저장할 아이디 입력 : ")
print("인증 프로그램 입니다.")
inputId = input("비교할 아이디 입력 : ")
if saveId==inputId:
    print("인증 통과!!!")
else :
    print("인증 실패!!!")
'''
'''
num = int(input("수 입력 : "))
if num%2 == 0:
    if num%3==0:  
        print("짝수이며 3의 배수이다.")
    else :
        print("짝수이다. 3의 배수는 아니다.")
else:
    print("아니다")
print("다음 문장들 실행")
'''

'''
#사용자로부터 GByte의 값을 입력받아 byte, Kbyte, Mbyte로 출력되게 만드시오.
volume = int(input("GByte를 입력하시오."))
Mbyte = volume*1024
Kbyte = Mbyte*1024
byte = Kbyte*1024
num = int(input("1.byte 2.Kbyte 3.Mbyte 선택 : "))

if num == 1:
    print(byte,"byte")
if num == 2:
    print(Kbyte,"Kbyte")
if num==3 :
    print(Mbyte,"Mbyte")
'''
#인증프로그램을 만드시오.
saveId = input("저장할 아이디 입력 : ")
savePw = input("저장할 비밀번호 입력 : ")
print("인증 프로그램 입니다.")
inputId = input("비교할 아이디 입력 : ")
inputPw = input("비교할 비밀번호 입력 : ")
if saveId==inputId:
    if inputPw == savePw:
        print("인증 통과")
    else :
        print("비밀번호가 틀렸습니다.")
else :
    print("등록 되지 않은 아이디 입니다.")


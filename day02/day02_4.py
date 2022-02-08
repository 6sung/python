name = input("학생 이름 : ")
sbj1 = int(input("국어 점수 : "))
sbj2 = int(input("영어 점수 : "))
sbj3 = int(input("수학 점수 : "))
sum_ = sbj1+sbj2+sbj3
avg = sum_/3
print("======================학생 정보======================")
print("이름\t국어\t영어\t수학\t합계\t평균")
print(name,"",sbj1,"     ",sbj2,"     ",sbj3,"     ",sum_,"     ",round(avg,2))

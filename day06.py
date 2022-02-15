print(10,'+',20,'=',30)
print('{}+{}={}'.format(10,20,30))

print('{2}+{0}={1}'.format(10,20,30))

print('{:,}'.format(1000000))

print('{:<10},{:0<10}'.format('첫번째','두번째'))
print('{:>10},{:a>10}'.format('첫번째','두번째'))
print('{:^10},{:a^10}'.format('첫번째','두번째'))
#list : 하나의 변수에 여러개의 값을 저장
ls = [10,20,30,40,50]
for i in ls:
    print(i, end=" ")
print()
st = "test 123"
for i in st:
    print(i)
st = "it is a fun Python class"
# 총개수(공백 포함) : 24
# a 개수 : 2
# s 개수 : 3
cnt_a = cnt_s = cnt = 0
for i in st:
    cnt += 1
    if i == 'a':
        cnt_a += 1
    elif i == 's':
        cnt_s += 1
print('총 개수 : {}, a 개수 : {}, s 개수 : {}'.format(cnt,cnt_a, cnt_s))

for i in range(0,3,1):
    print("--- 시작")
    for k in range(0,5,1):
        print('이중 for문 (i:{}, k:{})'.format(i,k))
    print("끝---")


for i in range(2,10,1):
    for k in range(1,10,1):
        print('{} * {} = {}'.format(i,k, i*k) )
'''
상위포문 0 일때 하위 포문 :0 0 0 0 0 
상위포문 1 일때 하위 포문 :0 1 2 3 4 
상위포문 2 일때 하위 포문 :0 2 4 6 8 
상위포문 3 일때 하위 포문 :0 3 6 9 12 
상위포문 4 일때 하위 포문 :0 4 8 12 16 
'''
for i in range(0,5):
    print()
    print('상위포문',i,'일때 하위 포문 :',end='')
    for k in range(0,5):
        print(i * k, end=' ')
'''
1   2   3    4    5
6   7   8    9    10
11 ...            15
16 ...            20
21 ...            25
'''
for i in range(1,22,5):
    for k in range(0,5):
        print(i+k, end="\t")
    print()

for i in range(0,5):
    for j in range(1,6):
        print(j+5*i, end="\t")
    print()









# 1-15 한줄의 마법

# 여러줄 if-else
num = 3

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 여러줄 result

number = 3

if number % 2 == 0:
    result = "짝수"
else:
    result = "홀수"

    print(f'{number}은 {result}입니다.')

# 한줄 요약 result

number_Reminder = 3

number_Reminder_result = ("짝수" if number_Reminder % 2 == 0 else "홀수")

print(f'{number_Reminder}은 {number_Reminder_result}입니다.')
# 설명 짝수라고 해라 만약(if) number_Reminder가 2로 나눴을때 나머지가 0으로 나오면 (else) 그렇지 않으면 홀수라고 해라 라는 뜻

# 반복문을 한줄로 쓰자

arrayList = [1,3,2,5,1,2]
# repeat_loop

b_list = []
for a in arrayList:
    b_list.append(a*2)

print(b_list)

# 한줄로 쓰자 ↑ 같은 구문이다.
b_list = [a*2 for a in arrayList]

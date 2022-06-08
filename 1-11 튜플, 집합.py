# 1-11 투플, 집합

a = ["사과","감","배"]

a[1] = "수박"
print(a)

a[1] = "사과" # 일반적으로 a[1] 배열에 재할당해서 들어갈 수 있음
print(a)

# 튜플형

a = ("감","배추","토마토")
print(a) # output: [감, 배추, 토마토]
print(a[1]) # output: 배추

# 그렇지만 재할당은 불가능하다 할 수 없다. 재할당을 시도하면 에러발생한다.

# Example
People = [{"name":"bob", "age": 27},{"name":"john","age":30}] # 재할당 변경가능
Person = [("bob",27),("john",30)] # 간편하게 사용할 수 있음

# 집합형
a = [1,2,3,4,5,6,7,8,9,0]
a_set = set(a)
print(a_set) # set(a)를 붙이면 자동적으로 배열을 만들어준다.

b = [1,2,3,4,5,6,6,6,5,5,5,4,4,3,2,1,0]
b_set = set(b) # {0, 1, 2, 3, 4, 5, 6}
print(b_set) # 중복된 수가 제거되고 배열을 순서대로 정렬되게 만들어 준다.

c = ["사과","감","배","수박","딸기"]
d = ["배","사과","포도","참외","수박"]

c_set = set(c)
d_set = set(d)

print(c_set & d_set) # 교집합 {'사과', '배', '수박'}
print(c_set | d_set) # 합집합 {'감', '딸기', '수박', '포도', '사과', '배', '참외'}

# 퀴즈
# a와 b의 "차집합" 구하는 방법을 구글링해보세요

subject_A = ["물리2","국어","수학1","음악","화학1","호학2","체육"]
subject_B = ["물리1","수학1","미술","화학2","체육"]

# 할때 무조건 set을 붙여서 정리한다. 
subJect_school1 = set(subject_A)
subJect_school2 = set(subject_B)

# 문제 풀이 방식 1번
print(subJect_school1 - subJect_school2) # 차집합 겹치는 부분 뺀다 output: {'음악', '호학2', '화학1', '물리2', '국어'}

# 문제 풀이 방식 2번
print(subJect_school1.difference(subJect_school2)) # 차집합 겹치는 부분 뺀다 output: {'음악', '호학2', '화학1', '물리2', '국어'}
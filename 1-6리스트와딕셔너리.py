# 리스트와 딕셔너리

a_list = ["사과","배","감"]
print(a_list)
print(a_list[0])
print(a_list[1])
print(a_list[2])

print()
print()

b_list = [2, "배", False, ["사과","감"]] # ["사과","감"]이 들어가 있는건 3번째 리스트라고 할 수 있다.
print(b_list) # [2, '배', False, ['사과', '감']]
print(b_list[0]) # 2
print(b_list[1]) # 배
print(b_list[2]) # False
print(b_list[3]) # ['사과', '감']
print(b_list[3][0]) # 사과
print(b_list[3][1]) # 감

# 추가할때 기능
c_List = [1,5,6,3,2]
c_List.append(99) # append(99)는 c_List속에 숫자 99를 추가함
c_List.append(100) # append(100)은 c_List속에 숫자 100을 추가함
print(c_List)

d_List = [1,5,6,3,2]
result = d_List[:3] # 앞에서 3개 배열만 자르기
print(result)
result2 = d_List[-1] # 뒤에서 첫번째를 자르기
print(result2)
result3 = d_List[-2] # 뒤에서 두번째를 추출
print(result3)
result4 = len(d_List)
print(result4) # 배열의 길이를 구하기
d_List.sort(reverse=True) # d_List.sort(reverse=True)는 배열의 순서가 오름차순의 반대인 내림차순으로 정렬
print(d_List)
d_List.sort(reverse=False) # d_list.sort(reverse=False)는 배열의 순서가 sort()만으로 오름차순인데 reverse는 반대인 내림차순 근데 이것을 False로 지정 결론 오름차순으로 지정함
print(d_List)
d_List.sort() # d_List.sort()는 배열의 오름차순으로 정렬할때 지정함
print(d_List)

result5 = (5 in d_List) # 5가 in(result) 안에 있는지 확인한다. 있을경우 True, 없을 경우 False
print(result5) # True

a_dict = {"name" : "bob","age":27}

sparta_Py_result1 = a_dict["name"] # a_dict의 "name"값을 출력하라고 할때 사용한다.
print(sparta_Py_result1) # 결과값은 bob
print(a_dict["name"]) # 결과 값은 bob

sparta_Py_result2 = a_dict["age"] # a_dict의 "age"값을 출력하라고 할때 사용한다.
print(sparta_Py_result2) # output: 27
print(a_dict["age"]) # output: 27

b_dict = {"name": "bob", "age" : 27, "friend": ["영희", "철수"]}
sparta_Py_result3 = b_dict["friend"]
print(sparta_Py_result3)# ["영희","철수"]
print(b_dict["friend"]) # ["영희","철수"]


sparta_Py_result4 = b_dict["friend"][1]
print(sparta_Py_result4) # output: 철수
print(b_dict["friend"][1]) # output: 철수

sparta_Py_result5 = b_dict["friend"][0]
print(sparta_Py_result5) # output: 영희
print(b_dict["friend"][0]) # output: 영희

c_dict = {"name": "bob", "age": 27, "friend": ["영희","철수"]}
c_dict["height"] = 180
# 만약에 c_dict의 list안에 height: 180이라는 값이 없는데 넣는 경우 c_dict["height"] = 180 으로 해서 넣으면 자동으로 생성된다.
print(c_dict) # output: name: bob, age: 27, friend: 영희, 철수, height: 180
print(c_dict["height"])

looking_for = ("height" in c_dict)
print(looking_for) # True
print("height" in c_dict) # True

people = [{"name": "bob","age": 27},
          {"name": "john", "age": 30}
]
print(people) # output: [{'name': 'bob', 'age': 27}, {'name': 'john', 'age': 30}]
print(people[0]) # output: {'name': 'bob', 'age': 27}
print(people[1]) # output: {'name': 'john', 'age': 30}
print(people[0]["name"]) # output: bob
print(people[1]["name"]) # output: john
print(people[0]["age"]) # output: 27
print(people[1]["age"]) # output: 30

# 퀴즈
" Smith의 Science 점수를 출력해보세요."

People_exam = [
    {"name": "bob", "age": 20, "score": {"math": 90, "science": 70}},
    {"name": "carry", "age": 38, "score": {"math": 40, "science": 72}},
    {"name": "smith", "age": 28, "score": {"math": 80, "science": 90}},
    {"name": "john", "age": 34, "score": {"math": 75, "science": 100}}
]

print(People_exam)
exam_score = People_exam[2]["score"]["science"]
# 만약 {"math","science"}을 넣으면 배열의 숫자로 봅을수있지만
#{"math": 80, "science":90}의 또 변수와 값이 있기때문에 배열로 찾는것이 아닌 "science"로 찾아야 한다.
print(exam_score)
print(People_exam[2]["score"]["science"])

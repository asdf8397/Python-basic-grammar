# 1-13 예외처리

# try - except문
# 에러가 있어도 건너뛰게 할 수 있는 방법

People = [
    {"name":"bob","age": 20},
    {"name":"carry","age": 38},
    {"name":"john","age": 7},
    {"name":"smith","age": 17},
    {"name":"ben","age": 27},
    {"name":"bobby","age": 57},
    {"name":"red","age": 32},
    {"name":"queen","age": 25}
]

for person in People:
    if person["age"] > 20:
        print(person["name"])

client_name_age = [
    {"name": "bob", "age": 20},
    {"name": "carry", "age": 38},
    {"name": "john", "age": 7},
    {"name": "smith", "age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby"}, # age가 bobby에 없을때 for문에서 사용해 줄수있는 것 예외처리 할 수 있음
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

# 예외처리 중간에 진행되다가 에러가 발생될 경우 에러처리에 대한 글을 넣어주고 뒤에 계속 진행 됨.
for name_age in client_name_age:
    try:
        if name_age["age"] > 20:
            print(name_age["name"])
    except:
        print(name_age["name"], "에러입니다.") # 많이 사용하면 나중에 에러 문제가 났을때 어디서 에러가 나온지 잘 모름

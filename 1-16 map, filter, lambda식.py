# 1-16 map, filter, lambda식

my_Client_list = [
    {"name": "bob","age": 20},
    {"name": "carry","age": 38},
    {"name": "john","age": 7},
    {"name": "smith","age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby", "age": 57},
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

# map - map을 이용해서 20보다 크면 adult 20보다 작으면 teenager

def check_adult(person):
    if person["age"] > 19:
        return "adult"
    else:
        return "teenager"

result_my_Client_check_list = map(check_adult, my_Client_list)
'map(function, iterable) - map(1,2) 2번 자리의 iterable에 들어가는 것은 처음 지정한 것은' \
'처음 지정한 배열 my_Client_list의 배열이 들어가고 이것들이 배열이 하나씩 분리되서 check_adult에' \
'들어가게 된다. def check_adult(person):에 진입하게 되고 if문을 따라 조건에 맞춰서 return되서 출력되고' \
'이것이 다시 result = map()괄호안에 들어와서 print(list(result))에 적용되게 된다.'
# print(result) # 만약 이대로 출력하게 되면 map object at 0x0000002E9D94DAFA0으로 출력되고 알아볼수없다 이럴때 list로 출력해야한다.

print(list(result_my_Client_check_list)) # 출력에서 print(list(result_my_Client_check_list))로 출력해야 배열로 출력이 됨

my_Client_list_divide = [
    {"name": "bob","age": 20},
    {"name": "carry","age": 38},
    {"name": "john","age": 7},
    {"name": "smith","age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby", "age": 57},
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

def divide_check_adult_teenager(standard):
    return ("성인" if standard["age"] > 19 else "청소년")

result_adult_teenager_divide = map(divide_check_adult_teenager, my_Client_list_divide)
# 헷갈리지 말것 def divide_check_adult_teenager이 map(1,2)에서 1번에 들어가야한다. standard가 들어가는 것이 아님
print(list(result_adult_teenager_divide))

# 람다식

my_Client_Name_age = [
    {"name": "bob","age": 20},
    {"name": "carry","age": 38},
    {"name": "john","age": 7},
    {"name": "smith","age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby", "age": 57},
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

'def my_Client_list(client_List):' \
    'return ("성인" if client_List["age"] > 19 else "청소년")'\

'result_lambda = map(my_Client_list, my_Client_Name_age)'\
'print(list(result_lambda))'
'↓'

# 람다식

result_lambda = (lambda client_List: ("성인" if client_List["age"] > 19 else "청소년"), my_Client_Name_age)
print(list(result_lambda))

# filter - filter는 true인 값만 출력되는 것

client_Name_Age_list = [
    {"name": "bob","age": 20},
    {"name": "carry","age": 38},
    {"name": "john","age": 7},
    {"name": "smith","age": 17},
    {"name": "ben", "age": 27},
    {"name": "bobby", "age": 57},
    {"name": "red", "age": 32},
    {"name": "queen", "age": 25}
]

Client_age_extraction = filter(lambda x: x["age"] > 19, client_Name_Age_list)
# x:x 자리에 다르게 변수명을 지정할 수 도 있지만 보통 x를 많이 사용한다.
print(list(Client_age_extraction))

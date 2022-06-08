# 1-17 함수 심화

def cal(a, b):
    return a+2*b

result = cal(1,2)
print(result) # output: 5

def calculator(a, b):
    return a+2*b

calculator_result = calculator(a=1, b=2)
# a=1, b=2 이렇게 지정해주면 결과는 같다 하지만 자리의 순서를 맞추지 않아도 된다.
print(result)

def cal_fix(a, b=2):
    return a+2*b

result_fix = cal_fix(1)
# 현재 cal_fix의 b=2 고정중이다 그래서 cal_fix(1)을 넣어주면 a에는 자동으로 들어갔다고 받아드린다.
# 그리고 cal_fix(1)을 넣어준 것과 cal_fix(a, b=2)의 고정된 값이 연산되서 결과값이 도출된다.
print(result_fix) # output: 5

def calculator_Change(a, b=2):
    return a+2*b

result_Change = calculator_Change(1,3)
# calculator_Change에 b=2 고정되어 있어도 calculator_Change(1,3)을 넣어줘서 새로 지정했기때문에 새로 지정한 값으로 연산이 된다.
print(result_Change) # output: 7

def calculator_Unlimited(*args): # *args를 지정하면 a,b처럼 지정한 값이 없다 다만 넣어줄때마다 무한대로 들어간다.
    for name in args:
        print(f'{name} 밥먹어라 얘드라')

    calculator_Unlimited('영수','철수','민지','지예','상철','민철')

# 키워드 인수를 여러가지를 받아보자

def calculator_several(**kwargs):
    print(kwargs)

    calculator_several(name = "bob",age = 30,height = 180)
    # 키워드 인수를 여러개를 받을때 사용함


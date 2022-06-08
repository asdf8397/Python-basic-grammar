# 1-12 f-string

scores = [
    {"name":"영수","score":70},
    {"name":"영희","score":65},
    {"name":"기찬","score":75},
    {"name":"희수","score":23},
    {"name":"서경","score":99},
    {"name":"미주","score":100},
    {"name":"병태","score":32}
]

for s in scores:
    print(s)

    name = s["name"]
    score = s["score"]
    print(name, score)
    
    # 여기서 문장에 배열안에 있는 내용을 넣어주고 싶을때
    #  문제: 영수의 점수는 100점 입니다.

    print(name +"의 점수는" + str(score)+"점입니다.")
    # string과 int는 더할수 없어서 syntex-error의 지속적 발생
    # str 또는 int를 넣어준다.

    # f-string - 간단하게 표현가능
    # f-string을 사용할때 ''을 그냥 사용하면 주석처리 그렇지만 앞에 f''을 사용하면 f-string 사용법임
    print(f'{name}의 점수는 {score}점입니다.') # 일반적으로 사용했는 방법이랑 다르지만 결과는 똑같음
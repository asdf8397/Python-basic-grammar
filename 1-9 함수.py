# 1-9 함수

def hello():
    print("안녕!")
    print("좋은 날씨야")


hello()
hello()

def sum(a,b):
    return a+b

result_sum = sum(1,2)
print(result_sum)

def sum_sum(a,b):
    print("더하기를 하셨네요!")
    return a+b

result_sum_Re = sum_sum(3,4)
print(result_sum_Re)

def bus_rate(age):
    if age > 65:
        print("노인우대 무료입니다.")
    elif age > 20:
        print("성인입니다 요금은 1200원입니다.")
    else:
        print("청소년입니다 요금은 950원입니다.")

bus_rate(70)

def bus_passenger_fare(age):
    if age > 65:
        return "노인우대 무료입니다."
    elif age > 20:
        return "성인입니다. 요금은 1200원입니다."
    else:
        return "청소년입니다. 요금은 950원입니다."

    passenger_fare = bus_passenger_fare(21)
    print(passenger_fare)
    
# 퀴즈
# 주민등록번호를 입력받아 성별을 출력하는 함수 만들기

def check_gender(my_number_social_number):
    my_Number = my_number_social_number("-")[1][:1]
    if int(my_Number) % 2 == 0:
        print("여성")
    else:
        print("남성")

    my_pin_Social_security_number3 = "200101-3012345"
    my_pin_Social_security_number2 = "200101-2012345"
    my_pin_Social_security_number4 = "200101-4012345"

    check_gender(my_pin_Social_security_number2)
    check_gender(my_pin_Social_security_number3)
    check_gender(my_pin_Social_security_number4)
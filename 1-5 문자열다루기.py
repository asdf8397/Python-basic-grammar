# 문자열 다루기

firstname = "dongyoung"
lastName = " Kim"

print(firstname + lastName) # dongyoung kim

a = 2
b = a

print(a) # 2
print(b) # 2

a2 = "2김"
b2 = a2

print(a2) # 2김
print(b2) # 2김

a3 = 2
b3 = 3

print(a3 + b3) # 5

a4 = "2"
b4 = "2"

print(a4 + b4) # 22

a5 = "2"
b5 = str(10)

print(a5 + b5) # 210

a6 = int("10")
b6 = 10

print(a6 + b6) # 20

# 문자열 다루기
text = "abcdefghijk"
result = text
print(text) # abcdefghijk
print(result) # abcdefghijk

text2 = "abcdefghijk"
result2 = len(text2)
print(result2) # 11

text3 = "abcdefghijk"
result3 = text3[:3] # abcdefghijk에서 앞의 3개만 나타낼때 사용 [:3]
print(result3) # abc
result4 = text3[3:] # abc 3개의 뒤부터 출력하고 싶을때
print(result4) # defghijk

text4 = "abcdefghijk"
result5 = text4[3:8]
print(text4[3:8]) # defgh
print(result5) # defgh

# 리스트 자르기

myEmail = "abc@sparta.com"
result6 = myEmail.split("@") # "abc","sparat.com으로 @구간의 사이로 글이 쪼개진다.
result7 = myEmail.split("@")[1]  # abc,sparat.com으로 나눠지는데 abc는 0번째 sparat.com은 1번째 여기서 sparat.com 1번째가 출력된다.
result8 = myEmail.split("@")[1].split(".") # @을 기준으로 abc, sparat.com으로 나눠지는데 sparta.com에서 sparta와 .을 기준으로 com으로 나눠짐
result9 = myEmail.split("@")[1].split(".")[0] # abc, sparta.com으로 나눠지고 .을 기준으로 sparat, com으로 나눠졌을때 0번째 sparat가 출력됨

print(result6) # output: "abc","sparat.com"
print(result7) # output: "sparta.com"
print(result8) # output: "sparta", "com"
print(result9) # output: "sparta"

# 퀴즈
# 1. 문자열의 앞의 반만 출력하기 "sparta"의 앞의 3글자인 "spa"만 출력해봅시다.

name = "sparta"
name_result = name
print(name_result[:3]) # spa
print(name[:3]) # spa

# 2. 전화번호의 지역번호 출력하기
phone = "02-123-1234"
print(phone[:2]) # 02
# 이렇게 출력 또는

phone_local_print = phone.split("-")[0]
print(phone_local_print)

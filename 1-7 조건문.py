# 1-6 조건문
# if () {}를 써주는게 아니라 :으로 사용해서 작성해주면 된다.
money = 5000

if money > 3800 :
    print("택시를 타자")
else:
    print("택시를 못타")

    print()
    print()
    
my_Pocket_money = 3000

if my_Pocket_money > 3800 :
    print("택시를 타자")
else: # else의 결과물이 print 2개인데 이것들이 나오게 하려면 print("택시를 못타") print("그럼 뭐 타지?")로 하면 된다.
    print("택시를 못타")
    print("그럼 뭐 타지?")

    print()
    print()
    
me_Pocket_money = 2000

if me_Pocket_money > 3800:
    print("택시를 타자")
elif me_Pocket_money > 1200: #elif는 JAVA와 JS의 else if와 같다고 할 수 있음
    print("버스를 타자")
else:
    print("걸어가자")
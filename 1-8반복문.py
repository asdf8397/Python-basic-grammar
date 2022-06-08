# 1-8 반복문

fruits = ["사과","배","감","수박","딸기"]

for pocket_in_my_fruit in fruits: # 반복문의 기초적인 문법
    print(pocket_in_my_fruit) # 사과, 배, 감, 수박, 딸기
    # pocket_in_my_fruits in fruits를 하면 fruits의 배열에 하나씩 꺼내서 pocket_in_my_fruits안에 넣는다.
    print(fruits) # [사과,"배","감","수박","딸기"]
    # fruits는 ["사과","배","감","수박","딸기"] 배열 전체를 집어 넣는 것


    people = [
        {'name': 'bob', 'age': 20},
        {'name': 'carry', 'age': 38},
        {'name': 'john', 'age': 7},
        {'name': 'smith', 'age': 17},
        {'name': 'ben', 'age': 27},
        {'name': 'bobby', 'age': 57},
        {'name': 'red', 'age': 32},
        {'name': 'queen', 'age': 25}
    ]

    print(people[0])
    print(people[0]["name"])
    print(people[0]["age"])


    print(people) # [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}, {'name': 'john', 'age': 7}, {'name': 'smith', 'age': 17}, {'name': 'ben', 'age': 27}, {'name': 'bobby', 'age': 57}, {'name': 'red', 'age': 32}, {'name': 'queen', 'age': 25}]

    for person_characteristic_list in people:
        print(person_characteristic_list)
        # 출력
        "[{'name': 'bob', 'age': 20}, " \
        "{'name': 'carry', 'age': 38}, " \
        "{'name': 'john', 'age': 7}, " \
        "{'name': 'smith', 'age': 17}, " \
        "{'name': 'ben', 'age': 27}, " \
        "{'name': 'bobby', 'age': 57}, " \
        "{'name': 'red', 'age': 32}, " \
        "{'name': 'queen', 'age': 25}]"

        list_Info = [
            {'name': 'bob', 'age': 20},
            {'name': 'carry', 'age': 38},
            {'name': 'john', 'age': 7},
            {'name': 'smith', 'age': 17},
            {'name': 'ben', 'age': 27},
            {'name': 'bobby', 'age': 57},
            {'name': 'red', 'age': 32},
            {'name': 'queen', 'age': 25}
        ]

        print("")
        print("")

        for person_list in list_Info:
            name = person_list["name"]
            age = person_list["age"]
            print(name, age)

            People_list_name_age = [
                {'name': 'bob', 'age': 20},
                {'name': 'carry', 'age': 38},
                {'name': 'john', 'age': 7},
                {'name': 'smith', 'age': 17},
                {'name': 'ben', 'age': 27},
                {'name': 'bobby', 'age': 57},
                {'name': 'red', 'age': 32},
                {'name': 'queen', 'age': 25}
            ]

            for detail_explanation in People_list_name_age:
                detail_name =  detail_explanation["name"]
                detail_age = detail_explanation["age"]
                # print(detail_name,detail_age)

                if detail_age > 20:
                    print(name, age)

            list_grammer = [
                {'name': 'bob', 'age': 20},
                {'name': 'carry', 'age': 38},
                {'name': 'john', 'age': 7},
                {'name': 'smith', 'age': 17},
                {'name': 'ben', 'age': 27},
                {'name': 'bobby', 'age': 57},
                {'name': 'red', 'age': 32},
                {'name': 'queen', 'age': 25}
            ]

            for i, People_name_age_list in enumerate(list_grammer): #enumerate(수를 세다)
                general_list_name = People_name_age_list["name"]
                general_list_age = People_name_age_list["age"]
                # print(general_list_name, general_list_age)
                print(i, general_list_name, general_list_age)\

                list_My_business_client = [
                    {'name': 'bob', 'age': 20},
                    {'name': 'carry', 'age': 38},
                    {'name': 'john', 'age': 7},
                    {'name': 'smith', 'age': 17},
                    {'name': 'ben', 'age': 27},
                    {'name': 'bobby', 'age': 57},
                    {'name': 'red', 'age': 32},
                    {'name': 'queen', 'age': 25}
                ]

                for i, business in enumerate(list_My_business_client):
                    client_name = business["name"]
                    client_age = business["age"]
                    print(i, client_name, client_age)
                    if i > 5: # i가 5보다 커질때 break에 걸린다.
                        break

                # 연습문제 /// 연습문제 잘 모르겠음 다시 한번 생각해볼 것
                "1. 짝수 출력하기"
                num_list = [1,2,3,6,3,2,4,5,6,2,4]

                for even_Number in num_list:
                    find_Even_numbers = even_Number
                    # print(find_Even_numbers[1])
                    # print(find_Even_numbers[3])
                    # print(find_Even_numbers[5])
                    # print(find_Even_numbers[6])
                    # print(find_Even_numbers[8])
                    # print(find_Even_numbers[9])
                    # print(find_Even_numbers[10])
                    " ↑ 이렇게 작성하면 오류를 발생 시킨다."

                    if find_Even_numbers % 2 == 0:
                        print(find_Even_numbers)
                        
                "2 리스트에서 짝수의 갯수를 출력하라"
                num_list_length = [1,2,3,6,3,2,4,5,6,2,4]

                count = 0
                for even_Number_length in num_list_length:
                    number_length = even_Number_length

                    if number_length % 2 ==0:
                        count += 1

                        print(count)
                        
                "3 리스트 안에 있는 모든 숫자 더하기"
                num_list_sum = [1,2,3,6,3,2,4,5,6,2,4]

                sum = 0
                for list_sum in num_list_sum:
                    sum = sum + list_sum

                    print(sum)
                    
                "4 리스트 안에 있는 자연수 중에 가장 큰 숫자 구하시오"

                num_List_big = [1,2,3,6,3,2,4,5,6,2,4]

                max = 0
                for num in num_list:
                    if max < num:
                        max = num

                        print(max)
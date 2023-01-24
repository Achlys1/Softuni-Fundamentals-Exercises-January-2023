n = int(input())
full_list = []

for _ in range(n):
    current_number = int(input())
    full_list.append(current_number)

command = input()

if command == "even":
    even_list = []
    for i in full_list:
        if i % 2 == 0 or i == 0:
            even_list.append(i)
    print(even_list)
elif command == "odd":
    odd_list = []
    for i in full_list:
        if i % 2 != 0:
            odd_list.append(i)
    print(odd_list)
elif command == "positive":
    positive_list = []
    for i in full_list:
        if i >= 0:
            positive_list.append(i)
    print(positive_list)
elif command == "negative":
    negative_list = []
    for i in full_list:
        if i < 0:
            negative_list.append(i)
    print(negative_list)

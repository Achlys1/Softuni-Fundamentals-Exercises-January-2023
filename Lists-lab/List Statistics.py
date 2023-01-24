n = int(input())
positive_list = []
negative_list = []
sum_negative = 0

for _ in range(n):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)

for i in negative_list:
    sum_negative += i

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}\nSum of negatives: {sum_negative}")

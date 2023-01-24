n = int(input())
word = input()
my_list = []
list_with_word = []

for i in range(n):
    current_sentence = input()
    my_list.append(current_sentence)

for i in range(len(my_list)):
    if word in my_list[i]:
        list_with_word.append(my_list[i])

print(my_list)
print(list_with_word)

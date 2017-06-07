# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

i = 0
new_list = []
while i < len(word_list):
    if any(char in x for x in word_list[i]):
        new_list.append(word_list[i])
        i = i + 1
    else:
        i = i + 1
print new_list

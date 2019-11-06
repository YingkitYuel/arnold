
list1 = []
for i in range(1,101):
    j = 0
    sum = 0
    while j <= i:
        sum +=j
        j += 1
    list1.append(sum)
print(list1)

num = input()
num1 = int(num)

for i in list1:
    j = 1
    if i == num1:
        print(i)
        break
    if i == list1[-1]:
        print('No')
        break
    j += 1
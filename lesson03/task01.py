n = int(input('Введи значение N: '))
num_list1 = []
for i in range(n):
  num = int(input())
  num_list1.append(num)
x = int(input('Введи значение X: '))
count = 0
for i in range(n):
  if x == num_list1[i]:
    count += 1
print(count)
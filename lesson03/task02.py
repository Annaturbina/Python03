n = int(input('Количество элементов в массиве: '))
num_list1 = []
for i in range(n):
  num = int(input())
  num_list1.append(num)
x = int(input('Число X: '))
nearest_number = num_list1[0]
for i in range(n):
  if abs(x - num_list1[i]) < abs(nearest_number - x):
    nearest_number = num_list1[i]
print(nearest_number)
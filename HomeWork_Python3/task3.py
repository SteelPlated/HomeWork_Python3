'''. Задайте список из вещественных чисел. Напишите
программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
max=0
min=1
list_1 = list(map(float, input("Введите числа через пробел:\n").split()))
for i in range(len(list_1)):
    a=list_1[i]
    list_1[i]=round(a-int(a),3)
    if list_1[i]>max:
        max=list_1[i]
    if list_1[i]<min:
        min=list_1[i]
print(max-min)

#arr = [1.1, 1.2, 3.1, 5, 10.01]
#arr = [x for x in arr if type(x) == float]
#arr_float = list()
#for i in arr:
#arr_float.append(round(i - int(i), 5))
#print(max(arr_float) - min(arr_float))

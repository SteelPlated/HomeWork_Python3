'''1. Задайте список из нескольких чисел. Напишите
программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 
3 и 9, ответ: 12'''

def SearchList(arr):
    s = 0
    for i in range(len(arr)):
        if i % 2 != 0:
            s += arr[i]
    print(f"Сумма равна: {s}")

list_1 = list(map(int, input("Введите числа через пробел:\n").split()))
SearchList(list_1)

#arr = [2, 3, 5, 9, 3, 5, 10]
#sum = 0
#for i in range(1, len(arr), 2):
#sum = sum + arr[i]
#print(sum)

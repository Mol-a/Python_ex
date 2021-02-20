
#4. Функция сортировки вставками insert:
# Цикл 1 – по i от 1 до N :					# i - текущая позиция при проходе по списку
# 	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
# 	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
# 	Цикл 2 – по j до 0 с шагом -1 :		# j - смещается справа налево, от больших к меньшим
# 		Условие если A[j-1]>t : 			# эл-ты отсортированной части, большие вставляемого
# 			Действие – A[j] = A[j-1] 		# уступают место – сдвигаются (копируются) вправо
# 		Иначе – выход из цикла 2		# j остановится на посл. эл-те, большем вставляемого
# 		Действие – A[j] = t				# вставляемый эл-т ставится на освободившееся место

import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика

def BubbleSort(A): # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def QuickSort(A, fst, lst): # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


def Sort_Insert(A):
    for i in range(1, len(A)):
        temp=A[i]
        j=i-1
        while (j >= 0 and temp < A[j]):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = temp

def Sort_shake(A):                  #разбор самостоятельный
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):  #слева направо перебираем
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
        for j in range (len(A)-2-j, j+1): #возвращаемся и перебираем справо налево
            if A[j-1] > A[j]:
                A[j], A[j - 1] = A[j - 1], A[j]

def Sort_shake2(A):             #алгоритм с функцией reversed переворачивание списка справо налево
    up = range(len(A) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                    swapped = True
            if not swapped:
                return A

def Sort_shake3(A):
    left = 0
    right = len(A) - 1

    while left <= right:                        #более понятный алгоритм с прохождением
        for i in range(left, right, +1):        #перебор слева направо
            if A[i] > A[i + 1]:                 #если левый элемент больше правого
                A[i], A[i + 1] = A[i + 1], A[i]
        right -= 1

        for i in range(right, left, -1):        #перебор справо налево
            if A[i - 1] > A[i]:                 #если левый(или следующий от правового) элемент больше правого
                A[i], A[i - 1] = A[i - 1], A[i]
        left += 1


table = prettytable.PrettyTable(["Размер списка", "Время пузырька", "Время быстрой", "Время вставки", "Время коктельной","Время коктельной_2", "Время коктельной_3"])
x=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]

for N in range(1000,5001,2000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

# print(A)
# print("000")

    C = A.copy()
    B = A.copy()
    D = A.copy()
    F = A.copy()
    G=A.copy()
    # # print(B)
    #
# BubbleSort(A)
#     # print("---")
# print(A)
    #
    #
# QuickSort(B, 0, len(B)-1)
    print("---")
# print(B)
#
# Sort_Insert(C)
# print("---")
# print (C)
#
# Sort_shake(D)
# print("---")
# print (D)
#
# Sort_shake2(F)
# print("---")
# print (F)
#
# Sort_shake3(G)
# print("---")
# print (G)

    t1 = datetime.datetime.now() #определяем время вначале
    BubbleSort(A)
    t2 = datetime.datetime.now() #определяем время после выполнения сортировки
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка " +str(N)+" заняла "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()#определяем время вначале
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()#определяем время после выполнения сортировки
    y2.append((t4 - t3).total_seconds())
    print("Быстрая " +str(N)+" заняла "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()#определяем время вначале
    Sort_Insert(C)
    t6 = datetime.datetime.now()#определяем время после выполнения сортировки
    y3.append((t6 - t5).total_seconds())
    print("Вставками " +str(N)+" заняла "+str((t6-t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()#определяем время вначале
    Sort_shake(D)
    t8 = datetime.datetime.now()#определяем время после выполнения сортировки
    y4.append((t8 - t7).total_seconds())
    print("Коктельная " +str(N)+" заняла "+str((t8-t7).total_seconds()) + "c")

    t9 = datetime.datetime.now()#определяем время вначале
    Sort_shake2(F)
    t10 = datetime.datetime.now()#определяем время после выполнения сортировки
    y5.append((t10 - t9).total_seconds())
    print("Коктельная_2 " +str(N)+" заняла "+str((t10-t9).total_seconds()) + "c")

    t11 = datetime.datetime.now()#определяем время вначале
    Sort_shake3(G)
    t12 = datetime.datetime.now()#определяем время после выполнения сортировки
    y6.append((t12 - t11).total_seconds())
    print("Коктельная_3 " +str(N)+" заняла "+str((t12-t11).total_seconds()) + "c")




    table.add_row([str(N), str((t2-t1).total_seconds()), str((t4-t3).total_seconds()), str((t6-t5).total_seconds()),str((t8-t7).total_seconds()),
                   str((t10-t9).total_seconds()),str((t12-t11).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4,"C56")
plt.plot(x, y5, "C85")
plt.plot(x, y6, "C89")


plt.show()
print(B)
print(D)



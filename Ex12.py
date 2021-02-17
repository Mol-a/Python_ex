#	Задание 1 Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?

a = int(input("Введите натуральное двузначное число:\n"))
if (a > 9 or a < 100):
    print("Число двузначное")
    if (a // 10 == 1 or a // 10 == 9 or a % 10 == 1 or a % 10 == 9):
        print("Число"+str(a)+" содержит цифры 1 или 9")
    else:
        print("Число "+str(a)+" не содержит цифры 1 или 9")
else:
    print("Число не двузначное");
# Задание 2
#3. О каждом учащемся класса известны его пол, год рождения, рост и вес. Определить, сколько в классе мальчиков и сколько девочек.
# Найти средний возраст мальчиков и девочек.
#Определить, верно ли, что самый высокий мальчик весит больше всех в классе, а самая маленькая девочка является самой юной среди девочек.
n = int(input("Введите размер списка:\n"))
A = []#создание пустого  списка (изменяемый, гибкий по размерности список) list
# A=() # создание пустого кортежа(неизменяемый список существующих значений) tuple
d=["Имя", "пол ученика (m-мужской, f-женский)", "год рождения", "рост", "вес"]
print(len(A), type(A))
for i in range(n):
    i=0
    K = []
    for x in range(5):
        info = input("Введите %s: \n"%(d[i]))
        K.append(info)
        i+=1
    print(K)
    A.append(K)
#print(len(A), type(A))
print(A)
#сколько в классе мальчиков и сколько девочек
man=[]
mans=[]
females=[]
for i in range(len(A)):
    if "m" in A[i]:
        man.extend(A[i])
        mans.append(A[i])

    if "f" in A[i]:
        females.append(A[i])
print("мальчиков %s \n" %(len(mans)))
print("девочек %s \n" %(len(females)))

#преобразование списков в кортежи
print(females)
f=tuple(tuple(i) for i in females)#преобразование вложенного списка девочек во вложенный кортеж
print(f)
print(mans)
mal=tuple(tuple(j) for j in mans)#преобразование вложенного списка мальчиков во вложенный кортеж
print(int(len(mal)), type(mal))
all=tuple(tuple(i)for i in A)
print (all)
#Найти средний возраст мальчиков и девочек
d=0
m=0
count_m=0
count2_f=0
for i in range(len(all)):
    old = 2021-int(all[i][2])
    if "m" in all[i]:
        m+=old
        count_m+=1
    if "f" in all[i]:
        d+=old
        count2_f+=1
avrg_m=m/count_m
avrg_f=d/count2_f
print(count_m)
print(count2_f)

print("средний возраст мальчиков %s\n" %(avrg_m))
print("средний возраст мальчиков %s\n" %(avrg_f))

#верно ли, что самый высокий мальчик весит больше всех в классе
rost=0
max_rost=0
min_rost=1000
vozrast=0
for i in range (len(A)):
    if "m" in A[i]:
        rost =A[i][3]
        if int(rost) > max_rost:
            max_rost=int(rost)
            max_weight=A[i][4]
    elif "f" in A[i]:
        rost = A[i][3]
        if int(rost) < min_rost:
            min_rost = int(rost)
            min_vozrast = 2021-int(A[i][2])

for i in range (len(A)):
    if A[i][4]> max_weight:
        k="самый высокий мальчик весит больше всех в классе"
    else:
        k="не верно, что самый высокий мальчик весит больше всех в классе"
    vozrast=2021-int(A[i][2])
    if vozrast > min_vozrast:
        f="не верно, что самая маленькая девочка является самой юной среди девочек"
    else:
        f="верно, что самая маленькая девочка является самой юной среди девочек"

print("максимальный рост %s" %(max_rost))
print("минимальный рост %s" %(min_rost))
print("вес высокого мальчика %s"%(max_weight))
print("возраст маленькой девочки %s"%(min_vozrast))
print(k)
print(f)


# Задание 3 Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).' \
# Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию, представленному в таблице ниже.
# Найти номер минимального элемента списка.
import random

a = int(input("Введите размер списка:\n"))
A = [random.randint(0, 100) for i in range(a)]
print(A)
k = 0
for i in range(1, a):
    if A[i] < A[k]:
        k = i
print(k);


lenght_edge=[]
def q_squares(lenght, widht, n=0):
    while lenght!=0 or widht!=0:
        if lenght==widht:
            lenght_edge.append(1)
            return q_squares(lenght-1, widht - 1, n + 1)
        if lenght<widht:
            lenght_edge.append(lenght)
            return q_squares(lenght, widht-1, n+1)
        if widht<lenght:
            lenght_edge.append(widht)
            return q_squares(lenght-widht, widht, n+1)

    print("Ребра квадратов %s\n" %(lenght_edge))
    print("Количество квардратов %s\n" %(len(lenght_edge)))


a = int(input("Введите длину прямоугольника(целое число):\n"))
b = int(input("Введите ширину прямоугольника(целое число):\n"))
q_squares(a, b)

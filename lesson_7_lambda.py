
#NOTE - функция
# def fun_1(x):
#     return x*2
# print(fun_1(3))
# print(fun_1)
# print(type(fun_1))



#NOTE - создание лямбды
# лямбда всегда возвращает значение
# lam_1 = lambda: 2
# print(lam_1)
# print(lam_1())
# print(type(lam_1))



#NOTE - использование общей переменной
# num_1 = 4
# lam_2 = lambda: num_1 * 2
# print(lam_2())



# передача лямбде значения
# lam_3 = lambda x : x * 2
# print(lam_3(5))



# передача лямбде несколько значений
# lam_4 = lambda x , y , z : (x + y + z) * 2
# print(lam_4(1,2,3))



# значение по умолчанию в лямбде
# lam_5 = lambda x , y = 1 , z = 0 : (x + y + z) * 2
# print(lam_5(5))




# обычное условие
# num_z1 = 2
# if(num_z1 < 10):
#     ans_1 = "yes"
# else:
#     ans_1 = "not"
# print(ans_1)




# условие в одну строку
# num_z2 = 15
# ans_2 = "yes" if(num_z2 < 10) else "not"
# print(ans_2)




# условие в лямбде
# lam_6 = lambda x , y :  x if(x < y) else x * y
# print(lam_6(5 ,3))




# лямбду можно не сохранять
# print(lambda: 9)
# print((lambda: 9)())
# print((lambda x:  x * 9)(3))




# лямбда в условие
# num_z3 = 15
# lam_ans_3 = (lambda x: x+7) if(num_z3 < 10) else (lambda z: z * 20)
# print(lam_ans_3(5))




# условие в лямбде где условие возврашает лямбду
# lam_7 = lambda w : (lambda x: x+7) if(w < 10) else (lambda z: z * 20)
# print(lam_7(15)(3))




#LINK -  map(fun, arr) - использует функцию fun к каждому элементу arr
# def fun_2(el):
#     print(el)
#     return el * 2
# arr = [1,2,3,4,5,6]
# чтобы map корректно работала её нужно вызывать в функции list
# arr = list(map(fun_2 , arr))
# print(type(arr))
# print(arr)




#LINK -  map - принимает до шесть списков
# x элемент первого списка , y элемент второго списка
# def fun_3(x ,y):
#     print(x , y)
#     return x + y

# arr_2 = [1,5,3,7,2]
# arr_3 = [9,4,3,8,3]

# arr_4 = list(map(fun_3 , arr_2 ,arr_3))

# print(arr_4)




#LINK - использование лямбды в функции map
# arr_5 = [1,5,3,7,2]
# arr_5 = list(map(lambda x: x*10 , arr_5))
# print(arr_5)




#LINK - перебираем два списка
# arr_1 = [1,5,3,7,2]
# arr_2 = [9,4,3,8,3]
# arr_3 = list(map(lambda x , y : x + y , arr_1 , arr_2))
# print(arr_3)




#LINK -  filter - он фильтрует
# arr_1 = [1,2,3,4,5,6]
# arr_3 = list(filter(lambda x: x % 2 == 0 , arr_1))
# print(arr_3)




#LINK -  умножаю каждый элемент списка который находится в списке
# arr_1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#          ]
# def fun_4(x):
#     print(x)
#     return list(map(lambda r: r * 2 , x))
# arr_3 = list(map(fun_4 , arr_1))
# print("---------------")
# print(arr_3)




#LINK -  тоже самое , но лямбда
arr_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
         ]

arr_3 = list(map(lambda arr_x : list(map(lambda n : n * 3 , arr_x)) , arr_1))
print(arr_3)




# дз
# номер 1
# дан список [1,2,3,4,5,6] чисел все числа которые равны 1, 2, 3 должны стать числом 0 

# номер 2
# дан список чисел и строк убрать все строки из списка

# номер 3
# даны два списка чисел которые имеют одинаковый размер 
# написать программу которая сравнивает элемент каждого списков и сохраняет самый большой
# пример: 
#     даны списки
#         ar1 = [1,3,6]
#         ar2 = [3,9,2]
#         ответ : [3,9,6]

# номер 4
# дан список в котором списки с числами ,кzаждое число списка умножить на num
# переменная num прибавляется на 1 с каждым новым списком (num изначально равен 2)


nested_lists = [[1, 2], [3, 4], [5, 6]]  
num = 2

def fun(x):
    num+=1
    return x + num
result = [list(map(lambda x: x * num, sublist)) for num, sublist in enumerate(nested_lists, start=num)]
print(result)

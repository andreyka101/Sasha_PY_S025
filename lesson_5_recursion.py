
# функция возвращает функцию
# def fun_1():
#     print("run fun_1()")
#     return fun_2()

# def fun_2():
#     print("run fun_2()")
#     return 5

# print(fun_1())



# функция возвращает функцию и передаёт ей значение
# def fun_3(num_3_loc):
#     num_3_loc += 1
#     print("run fun_3() =" , num_3_loc)
#     return fun_4(num_3_loc)

# def fun_4(num_4_loc):
#     num_4_loc *= 2
#     print("run fun_4() =" , num_4_loc)
#     return num_4_loc

# print(fun_3(5))



# рекурсия - функция возвращает саму себя
# num_1 = 10
# def fun_5():
#     global num_1
#     num_1 -= 1
#     print(num_1)
#     if(num_1 > 0):
#         return fun_5()
#     print("end")
#     return num_1
    
# print(fun_5())
# print(num_1)
# fun_5()



# функция возвращает саму себя и передаёт себе же изменённое значение
# def fun_6(num_loc):
#     # print(num_loc)
#     if(num_loc > 0):
#         return fun_6(num_loc - 1)
#     print("end")
#     return num_loc
# print(fun_6(10))



# тоже саме, но обрабатываем дополнительную переменную sum_answer
# def fun_7(num_loc , sum_answer = 0):
#     print(num_loc)
#     if(num_loc > 0):
#         return fun_7(num_loc - 1 , sum_answer + num_loc )
#     print("end")
#     return sum_answer
# print(fun_7(10))



# рекурсия обрабатывает список
# def fun_8(arr_loc:list , answer = 0 , index = 0):
#     if(index != len(arr_loc)):
#         return fun_8(arr_loc , answer + arr_loc[index] , index + 1)
#     return answer

# arr = [1,2,3,4,5]
# print(fun_8(arr))






# дз
#TODO - номер 1
# Напишите функцию для вычисления факториала числа

#LINK - пример
# def fun(num , save = 1):
#     if(num > 0):
#         # print(index)
#         return fun(num - 1 , save * num)
#     return save
# print(fun(6))



#TODO - номер 2
# Напишите программу для возведения числа n в степень m. 
# нельзя использовать степень (**)

#LINK - пример
# def fun(num , index , save = 1):
#     if(index > 0):
#         # print(index)
#         return fun(num , index - 1 , save * num)
#     return save
# print(fun(2 , 3))


#TODO - номер 3
# напишите функцию которая принимает список чисел , 
# функция возвращает список где каждое значение было умножено на 2



#TODO - номер 4
# напишите функцию которая принимает два списка одинаковой длины.
# Необходимо создать из них словарь таким образом, 
# чтобы элементы первого списка были ключами, 
# а элементы второго — соответственно значениями нашего словаря.
# функция возвращает словарь

#LINK - пример
# def array(arr,arr_2 , index = 0 , save_dist = {}):
#     if len(arr) != len(arr_2):
#         return None
#     print("1")
#     print("1")
#     print("1")
#     print("1")
#     print("1")
#     print("1")  
# obj = {}
# index = 0
# arr_1s = [1,2,3,4]
# arr_2s = [9,7,6,5]
# obj[arr_1s[index]] = arr_2s[index]



#TODO - номер 5
# Напишите функцию которая принимает список с числами и строками и возвращает список с удалёнными строками
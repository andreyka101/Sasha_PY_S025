# операторы присваивания 
# print(4)
# num = 7
# num = 2
# num = num + 8
# num += 2
# num -= 2

# num_2 = None



# получаем тип
# print(type(num))



# типы
# print("int" , 5)
# print("float" , 5.0)
# print("str" , "text")
# print("bool" , True)
# print("null" , None)



# получаем символ строки через for
# str_a = "hello"
# print(str_a)
# for sym in str_a:
#     print(sym)




# функция это переменная
# def fun_1() -> str:
#     print("hello")
#     return 4

# print(fun_1)
# print(type(fun_1))
# print(fun_1())




# def fun_2(x:int):
#     return 4 * x
# print(fun_2(" wert"))





num = 8
def fun_3():
    # создаем свою локальную переменную num
    num = 20
    print(num)
fun_3()
print("num =" , num)




# # num = 8
# def fun_4():
#     # изменение глобальной переменной в функции
#     global num
#     num = 20
#     print(num)
# fun_4()
# print("num =" , num)




# у каждой функции своя локальная переменная
# num = 8
# def fun_5():
#     # print("fun4_1 =" , num)
#     num = 20
#     print("fun4_2 =" , num)
#     def fun6():
#         # print("fun5_1 =" , num)
#         num = 30
#         print("fun5_2 =" , num)
#     fun6()
        
# fun_5()
# print("num =" , num)




# def fun_4():
#     # создание глобальной переменной в функции
#     # global num
#     num = 20
#     print(num)
# fun_4()
# print("num =" , num)









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











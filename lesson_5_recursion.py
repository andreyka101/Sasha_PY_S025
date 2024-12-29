# def fun_1():
#     print("run fun_1()")
#     return fun_2()

# def fun_2():
#     print("run fun_2()")
#     return 5

# print(fun_1())



# def fun_3(num_3_loc):
#     num_3_loc += 1
#     print("run fun_3() =" , num_3_loc)
#     return fun_4(num_3_loc)

# def fun_4(num_4_loc):
#     num_4_loc += 1
#     print("run fun_4() =" , num_4_loc)
#     return num_4_loc

# print(fun_3(5))



# num_1 = 10
# def fun_5():
#     global num_1
#     num_1 -= 1
#     if(num_1 > 0):
#         return fun_5()
#     print("end")
#     return num_1
    
# print(fun_5())
# print(num_1)




# def fun_6(num_loc):
#     num_loc -= 1
#     print(num_loc)
#     if(num_loc > 0):
#         return fun_6(num_loc)
#     print("end")
#     return num_loc
# print(fun_6(10))




# def fun_8(num_loc , sum_answer = 0):
#     num_loc -= 1
#     # print(num_loc)
#     if(num_loc > 0):
#         return fun_8(num_loc , sum_answer + num_loc )
#     print("end")
#     return sum_answer
# print(fun_8(10))




# def fun_8(num_loc , sum_answer = 0):
#     num_loc -= 1
#     # print(num_loc)
#     if(num_loc > 0):
#         return fun_8(num_loc , sum_answer + num_loc )
#     print("end")
#     return sum_answer
# print(fun_8(10))




def fun_8(arr_loc:list , answer = 0 , index = 0):
    if(index != len(arr_loc)):
        return fun_8(arr_loc , answer + arr_loc[index] , index + 1)
    return answer

arr = [1,2,3,4,5]
print(fun_8(arr))




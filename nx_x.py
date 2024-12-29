obj = {
    1:1,
    8:2,
    27:3,
    64:4,
    125:5,
    216:6,
    343:7,
    512:8,
    729:9,
    1000:10
}
# for i in range(1 , 10):



# 3
def dictionary_from_string(mystring: str):

    if len(mystring) == 0:
        print("mystring can't be null")
        return
    
    mydict = {}
    
    for i in range(len(mystring)):
        mydict[mystring[i]] = i

    print(mydict)


# 4

arr_1 = ["q" ,"w" ,"e","r" , "t"]
arr_2 = [1,2,3,4,5]
mydict = {}
for i in range(len(arr_1)):
    mydict[arr_1[i]] = arr_2[i]
print(mydict)




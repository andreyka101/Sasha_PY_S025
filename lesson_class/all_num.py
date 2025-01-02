num_int = 5

num_str = "qwerr"

arr = [1,2,3,4]


def fun():
    print("ok")


class Dogs():
    '''это сообщение'''
    # init - вызывается при создании класса
    # self - это хранилище переменных и методов
    def __init__(self , name_loc):
          print("start class Dogs")
        #   создание переменной
          self.num = 7
        #   использование переменной
          print(self.num)
          print(name_loc)
          self.name = name_loc
          self.eat_num = 0
    # создание метода
    def run(self):
         print("run run run")
        #  self.eat_fun()
    # метод изменяет переменную
    def eat_fun(self , number = 2):
        '''это сообщение для метода'''
        self.eat_num += number
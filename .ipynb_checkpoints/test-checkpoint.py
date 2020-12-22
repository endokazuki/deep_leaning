class my_status:
    def __init__(self,age,name,height,weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight
        #インスタンスの初期化
        #例）self.age=null
        #       ↓←age=20(インスタンス変数self.ageに引数ageを取る)
        #    self.age=20

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)

    def print_height(self):
        print(self.height)

    def print_weight(self):
        print(self.weight)

a = my_status(34,"yamada",170,78)
print(a.age)
#class my_statusのself.ageを出力
b = my_status(34,"yamada",170,78).print_age
print(b)
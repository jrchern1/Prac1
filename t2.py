# 汽車類別
class Cars:
    door = 4  #類別屬性
    # 實體方法(Instance Method)
    def drive(self):
        self.__class__.door = 5
        self.door=6

print("Cars original door: ", Cars.door)
mazda = Cars()
mazda.drive()
print("Cars new door: ", Cars.door)
print("mazda's door=", mazda.door)
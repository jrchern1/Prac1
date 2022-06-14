# 汽車類別
class Cars:
    door = 4  # 類別屬性
    # 類別方法(Class Method)
    @classmethod
    def open_door(cls):
        print(f"{cls} has {cls.door} doors.")
mazda = Cars()
mazda.open_door()  #透過物件呼叫
Cars.open_door()  #透過類別呼叫
# 定義父類別
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # 功能定義在子類別


# 定義子類別，繼承自Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# 創建子類別的案例
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())

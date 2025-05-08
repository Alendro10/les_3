class superhero :
    count_super = 0
    def __init__(self, height = 180, power = 10, tool = "Nothing", age = 18):
        self.height= height
        self.power = power
        self.tool = tool
        self.age = age
        superhero.count_super += 1
        print(self.height)
        print(self.power)
        print(self.tool)
        print(self.age)
        print("")
Captain_America = superhero(height = 188, power=1000, tool="shield", age = 117)
Wonder_Woman = superhero(height = 178, power=3000, tool="lasso", age = 5000)
print(superhero.count_super)
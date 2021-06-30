class People:
    def __init__(self, name):
        self.name = name

list = []

list.append(People("scott"))
list.append(People("paul"))
list.append(People("jack"))
list.append(People("ryan"))

for i in range(len(list)-1):
    print(list[i].name)


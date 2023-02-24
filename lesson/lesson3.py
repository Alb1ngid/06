# инкапсуляция
# 1 публичный
# 2 защищенный
# 3 скрытый
class Bank:
    def __init__(self, name, age, key, a):
        self.name = name
        self.age = age
        self.__si = key
        self._a = a

    def set_key(self):
        print(self.__si)

    def get_key(self, a):
        self.__si = a

    def __str__(self):
        return f'{self.name} {self.age}'

    def __x2(self):
        self.age *= 2
        print(self.age)

    def x(self):
        self.__x2()


beka = Bank('beka', 19, 'qw23rgf4d3w1', 'a')
# print(beka)
# beka.x()
beka._a = '111111111111'
print(beka._a)

print(...)
# beka.get_key('222222222')
# beka.set_key()
# print(beka)
# beka.__x2()
print(Bank.mro())
print(dir(beka))
beka._Bank__si = "234554"
beka._Bank__x2()
beka.set_key()


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks
        # self.gotmarks = 'моё имя ' + self.name + ' мои оценки ' + self.mark

    @property
    def gotmarks(self):
        return 'моё имя ' + self.name + ' мои оценки ' + self.mark

    @gotmarks.setter
    def gotmarks(self, sent):
        name, rand, mark = sent.split(' ')
        self.name = name
        self.mark = mark


st = Student('beka', "99")
print(st.name)
print(st.mark)
print(st.gotmarks)
print('##########')
st.name = 'Zima blue'
print(st.name)
print(st.gotmarks)
print('##########')
st.gotmarks = 'Раст мои_оценки 66'
print(st.name)
print(st.mark)
print(st.gotmarks)

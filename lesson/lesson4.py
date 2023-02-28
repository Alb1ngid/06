# множественное наследование
# mro-metod resolution order,порядок выполнения методов
class A:
    def __init__(self, name):
        self.name = name

    def fly(self=True):
        print('A летает')


class B(A):
    def fly(self=True):
        print('B летает')


class V:
    def __init__(self, age):
        self.age = age

    def v(self=True):
        print('это меtод V')


class C(B, V):
    def __init__(self, name, age):
        B.__init__(self, name)
        V.__init__(self, age)

    def fly(self=True):
        print(B.fly())


print(C.mro())
c = C('name', 19)
print(c.name, c.age)

c.fly()
c.v()


class SA: ...


class CA: ...


class S: ...


class B: ...


class RE: ...


class Sec(S, B): ...


class BA(SA, CA): ...


class IB(BA, Sec): ...


class In(BA, RE): ...


class Asset(BA, RE, CA): ...

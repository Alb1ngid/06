class A:
    def info(self):
        print('это А')

class B(A):
    def info(self):
        super().info()


class C(B):
    def Info(self):
        print('это С')

class V(C):
    def info(self):
        super().info()

v=V()
v.info()
class Calculator:
    def __init__(self, value):
        self.value = value

    def operation(self):
        print("Выполнение операций")


class Multiple(Calculator):
    def __init__(self, value, x):
        self.value = value
        self.x = x

    def operation(self):
        print("Функция умножения равна:", self.value * self.x)


class Division(Calculator):
    def __init__(self, value, x):
        self.value = value
        self.x = x

    def operation(self):
        if self.x != 0:
            print("Функция деления равна:", self.value // self.x)
        else:
            print("Функция не выполнена. Знаменатель при делении не должен равняться нулю!")


class Summa(Calculator):
    def __init__(self, value, x):
        self.value = value
        self.x = x

    def operation(self):
        print("Функция сложения равна:", self.value + self.x)


class Difference(Calculator):
    def __init__(self, value, x):
        self.value = value
        self.x = x

    def operation(self):
        print("Функция разности равна:", self.value - self.x)


n, m = map(int,input("Введите первое и второе числа: ").split())
num1, num2 = Multiple(n, m), Summa(n, m)
number3, number4 = Division(n, m), Difference(n, m)
chislo = Calculator(n)
rez = [num1, num2, number3, number4, chislo]

for i in rez:
    i.operation()

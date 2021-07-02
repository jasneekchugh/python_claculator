def addition(a, b):
    return a + b


def subtraction(a, b):
    return b - a


def multiplication(a, b):
    return a * b


def div(a, b):
    return round((b / a), 9)


def sqrt(a):
    return round(a ** (1 / 2), 8)


def square(a):
    return a * a


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def div(self, a, b):
        self.result = div(a, b)
        return self.result

    def sqrt(self, a):
        self.result = sqrt(a)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

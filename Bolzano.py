import numpy as np


class Bolzano:
    def __init__(self, f):      # f is a list which contains the coefficients of the polynomial
        self.data = f
        self.grade = len(self.data) - 1

    class RootFound(Exception):
        pass

    def func_output(self, n):
        output = self.data[-1]
        for pos, num in enumerate(self.data[:len(self.data) - 1]):
            output += num * n ** (self.grade - pos)
        return output

    def sign(self, n):
        if self.func_output(n) == 0:
            raise self.RootFound
        else:
            return True if self.func_output(n) > 0 else False

    def solve(self, n, m, h=1.0):
        original_sign = self.sign(n)
        try:
            for i in np.arange(n + h, m, h):
                try:
                    if self.sign(i) != original_sign:
                        return self.solve(i - h, i + 0.1, h / 10)
                except self.RootFound:
                    return i
        except ValueError:
            return n


fn = Bolzano([1, 0, 3, 2])
print(fn.solve(-1, 1))

class Sort_Minority:
    def __init__(self, n, tuples):
        self.n = n
        self.tuples = tuples

    def func_sort_2(self, _tuples):
        x = self.tuples[0]
        y = self.tuples[1]
        if x > y:
            temp = x
            x = y
            y = temp
        return x, y

    def func_sort_3(self, _tuples):
        n = self.n
        tuples = self.tuples
        tuples[: n - 1] = self.func_sort_2(_tuples[: n - 1])
        tuples[n - 1:] = self.func_sort_2(_tuples[n - 1:])
        tuples[: n - 1] = self.func_sort_2(_tuples[: n - 1])

        return tuples

    def func_sort_4(self, _tuples):
        n = self.n
        tuples = self.tuples
        tuples[: n - 1] = self.func_sort_3(_tuples[: n - 1])
        tuples[n - 1:] = self.func_sort_3(_tuples[n - 1:])
        tuples[: n - 1] = self.func_sort_3(_tuples[: n - 1])

        return tuples

    def func_sort_5(self, _tuples):
        n = self.n
        tuples = self.tuples
        tuples[: n - 1] = self.func_sort_4(_tuples[: n - 1])
        tuples[n - 1:] = self.func_sort_4(_tuples[n - 1:])
        tuples[: n - 1] = self.func_sort_4(_tuples[: n - 1])

        return tuples

    def func_sort_6(self, _tuples):
        n = self.n
        tuples = self.tuples
        tuples[: n - 1] = self.func_sort_5(_tuples[: n - 1])
        tuples[n - 1:] = self.func_sort_5(_tuples[n - 1:])
        tuples[: n - 1] = self.func_sort_5(_tuples[: n - 1])

        return tuples


if __name__ == '__main__':
    number = 0
    tuple_s = tuple()
    opt = Sort_Minority(number, tuple_s)
    opt.func_sort_6(tuple_s)

class Sort_minority:
	def __init__(self, n, tuples):
		self.n = n
		self.tuples = tuples


def func_sort_2(tuples):
	x = tuples[0]
	y = tuples[1]
	if x > y:
		temp = x
		x = y
		y = temp
	return x, y


def func_sort_3(n, tuples):
	tuples[: n-1] = func_sort_2(tuples[: n-1])
	tuples[n-1:] = func_sort_2(tuples[n-1:])
	tuples[: n-1] = func_sort_2(tuples[: n-1])

	return tuples


def func_sort_4(n, tuples):
	tuples[: n-1] = func_sort_3(tuples[: n-1])
	tuples[n-1:] = func_sort_3(tuples[n-1:])
	tuples[: n-1] = func_sort_3(tuples[: n-1])

	return tuples


def func_sort_5(n, tuples):
	tuples[: n-1] = func_sort_4(tuples[: n-1])
	tuples[n-1:] = func_sort_4(tuples[n-1:])
	tuples[: n-1] = func_sort_4(tuples[: n-1])

	return tuples


def func_sort_6(n, tuples):
	tuples[: n-1] = func_sort_5(tuples[: n-1])
	tuples[n-1:] = func_sort_5(tuples[n-1:])
	tuples[: n-1] = func_sort_5(tuples[: n-1])

	return tuples


def func_sort_7(n, tuples):
	tuples[: n-1] = func_sort_6(tuples[: n-1])
	tuples[n-1:] = func_sort_6(tuples[n-1:])
	tuples[: n-1] = func_sort_6(tuples[: n-1])

	return tuples


def func_sort_8(n, tuples):
	tuples[: n-1] = func_sort_7(tuples[: n-1])
	tuples[n-1:] = func_sort_7(tuples[n-1:])
	tuples[: n-1] = func_sort_7(tuples[: n-1])

	return tuples


def func_sort_9(n, tuples):
	tuples[: n-1] = func_sort_8(tuples[: n-1])
	tuples[n-1:] = func_sort_8(tuples[n-1:])
	tuples[: n-1] = func_sort_8(tuples[: n-1])

	return tuples


if __name__ == '__main__':
	func_sort_9(n, tu)

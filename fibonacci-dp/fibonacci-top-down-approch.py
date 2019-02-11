import timeit


def fib_with_dp(_input, memo={}):
    if _input in memo.keys():
        return memo[_input]
    if _input in [1, 2]:
        memo[_input] = 1
        return 1
    else:
        output = fib_with_dp(_input - 1, memo) + fib_with_dp(_input - 2, memo)
        memo[_input] = output
        return output


def fib_without_dp(_input):
    if _input in [1, 2]:
        return 1
    else:
        output = fib_without_dp(_input - 1) + fib_without_dp(_input - 2)
        return output


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


if __name__ == '__main__':
    wrapped = wrapper(fib_without_dp, 5)
    print("Time taken by solving not using DP ==> " + str(timeit.timeit(wrapped)))

    wrapped = wrapper(fib_with_dp, 5)
    print("Time taken by solving using DP ==> " + str(timeit.timeit(wrapped)))

import multiprocessing as mp

from parallel_utilities.map import parallel_map, parallel_map_async


def fun(x: int) -> int:
    return x ** 2


def fun_tuple(x: tuple) -> tuple:
    return (x[0] ** 2, x[1] ** 2)


def test_parallel_map_simple():
    data = [1, 2, 3, 4, 5] * 3

    actual = parallel_map(data, fun)
    expect = [fun(x) for x in data]

    assert actual == expect


def test_parallel_map_tuple():
    data = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] * 3

    actual = parallel_map(data, fun_tuple)
    expect = [fun_tuple(x) for x in data]

    assert actual == expect


def test_parallel_map_async_simple():
    data = [1, 2, 3, 4, 5] * 3

    actual = parallel_map(data, fun)
    expect = [fun(x) for x in data]

    assert actual == expect


def test_parallel_map_async_tuple():
    data = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] * 3

    actual = sorted(parallel_map_async(data, fun_tuple))
    expect = sorted([fun_tuple(x) for x in data])

    assert actual == expect
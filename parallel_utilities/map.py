from typing import Callable, Iterable
import multiprocessing as mp


def parallel_map(data: Iterable, fun: Callable, n_cpus: int = 2) -> list:
    with mp.Pool(n_cpus) as pool:
        results = [pool.apply(fun, args=(x,)) for x in data]
    return results


def parallel_map_async(data: Iterable, fun: Callable, n_cpus: int = 2) -> list:
    with mp.Pool(n_cpus) as pool:
        result_objects = [pool.apply_async(fun, args=(x,)) for x in data]
        results = [r.get() for r in result_objects]
    return results
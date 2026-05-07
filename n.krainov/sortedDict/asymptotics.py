import time
import random
import math
import matplotlib.pyplot as plt
import matplotlib
from typing import Callable, Any
from sortedDict import SortedDict


def benchmark_operation(op : Callable[[SortedDict[int, str], int], Any],
                        d : SortedDict[int, str],
                        keys : list[int],
                        iterations : int = 1) -> float:
    start : float = time.perf_counter()
    for _ in range(iterations):
        for k in keys:
            op(d, k)
    end : float = time.perf_counter()
    return (end - start) / (iterations * len(keys))


def run_benchmark(type : str, sizes : list[int], iterations : int = 10) -> dict[str, list[float]]:
    results : dict[str, list[float]] = {'size': [], 'insert': [], 'search': [], 'delete': []}

    keys: list[int] = []
    for n in sizes:
        if type == 'random':
            keys = list(range(n))
            random.shuffle(keys)
        elif type == 'ascending':
            keys = list(range(n))
        elif type == 'descending':
            keys = list(range(n - 1, -1, -1))


        d : SortedDict[int, str] = SortedDict[int, str]()
        insert_time : float = benchmark_operation(
            lambda d , k : d.__setitem__(k, str(k)),
            d, keys, iterations
        )

        search_time : float = benchmark_operation(
            lambda d, k: d.__getitem__(k),
            d, keys, iterations
        )

        del_keys : list[int] = list(keys)
        random.shuffle(del_keys)
        delete_time : float = benchmark_operation(
            lambda d, k: d.__delitem__(k),
            d, del_keys, 1
        )

        results['size'].append(n)
        results['insert'].append(insert_time)
        results['search'].append(search_time)
        results['delete'].append(delete_time)
        print(f"{type:12s} n={n:6d}  insert: {insert_time:.3e} s/key  "
              f"search: {search_time:.3e} s/key delete: {delete_time:.3e} s/key")

    return results


def plot_results(all_results: dict[str, dict[str, list[float]]]) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    operations : list[str] = ['insert', 'search', 'delete']
    colors : dict[str, str] = {'random': 'blue', 'ascending': 'green', 'descending': 'red'}

    for op_idx, op in enumerate(operations):
        ax : Any = axes[op_idx]
        for dtype, results in all_results.items():
            xs : list[float] = [math.log2(n) for n in results['size']]
            ys : list[float] = results[op]
            ax.plot(xs, ys, '-o', color=colors[dtype], label=dtype)
        ax.set_title(f'Average time per key: {op}')
        ax.set_xlabel('log₂(n)')
        ax.set_ylabel('Time (s)')
        ax.legend()
        ax.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    sizes : list[int] = [10000, 20000, 50000, 100000, 1000000]
    random.seed(42)

    all_results : dict[str, dict[str, list[float]]] = {}
    for dtype in ['random', 'ascending', 'descending']:
        print(f"\n=== Benchmark for {dtype} keys ===")
        all_results[dtype] = run_benchmark(dtype, sizes, iterations=2)

    plot_results(all_results)
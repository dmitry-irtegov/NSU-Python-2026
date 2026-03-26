import time


class Timer:
    def __init__(self):
        self._start = None
        self._elapsed = None

    def __enter__(self):
        self._start = time.perf_counter()
        self._elapsed = None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._elapsed = time.perf_counter() - self._start
        print(f"Time elapsed: {self._elapsed:.1f} s")
        return False

    def get_value(self):
        if self._start is None:
            return None
        if self._elapsed is not None:
            return self._elapsed
        return time.perf_counter() - self._start

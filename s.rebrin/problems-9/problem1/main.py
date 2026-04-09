import time
from typing import Optional, Type


class Timer:
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc: Optional[BaseException], tb
    ) -> None:
        end = time.perf_counter()
        self.elapsed = end - self.start
        label = f"[{self.name}] " if self.name else ""
        print(f"{label}Elapsed time: {end - self.start:.6f} seconds")

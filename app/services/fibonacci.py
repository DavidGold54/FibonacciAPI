from functools import lru_cache

import numpy as np


@lru_cache(maxsize=1024)
def calculate_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        A = np.array([[1, 1], [1, 0]], dtype=object)
        m = n - 1
        # 指数計算
        result = np.identity(len(A), dtype=object)
        base = A
        while m > 0:
            if m % 2 == 1:
                result = np.dot(result, base)
            base = np.dot(base, base)
            m //= 2
        return result[0][0]
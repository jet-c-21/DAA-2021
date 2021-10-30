import random
from copy import deepcopy

from find_inversion import get_inversion
from find_inversion_ref import mergeSortInversion


def gen_int_array(size: int, seed=777, start=1, end=100):
    random.seed(seed)
    result = list()
    for _ in range(size):
        result.append(random.randint(start, end))
    return result


X = gen_int_array(100)
ans = mergeSortInversion(deepcopy(X), len(X))

y = get_inversion(deepcopy(X))
print(ans, len(y))
print(ans == len(y))

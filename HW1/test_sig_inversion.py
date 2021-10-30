from copy import deepcopy
import random

from significant_inversion_ver3 import get_sig_inversion
from significant_inversion_ref import mergeSortSigInversion


def gen_int_array(size: int, seed=777, start=1, end=100):
    random.seed(seed)
    result = list()
    for _ in range(size):
        result.append(random.randint(start, end))
    return result


X = gen_int_array(100)
print(f"original X:\n{X}\n")
ans = mergeSortSigInversion(deepcopy(X), len(X))

a = deepcopy(X)
pairs, sls = get_sig_inversion(a)
print(len(pairs) == ans)
print(len(pairs))
# print(sls == sorted(X))

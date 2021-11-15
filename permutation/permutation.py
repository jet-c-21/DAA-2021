from itertools import permutations as py_permute

def permutation(seq: list, k: int, n: int):
    if k == n - 1:
        for i in range(n):
            print(seq[i], end='')
        print()

    else:
        for i in range(k, n):
            temp = seq[k]
            seq[k] = seq[i]
            seq[i] = temp

            permutation(seq, k + 1, n)

            temp = seq[k]
            seq[k] = seq[i]
            seq[i] = temp


# !/usr/bin/env python
def perm(n, i):
    if i == len(n) - 1:
        print(n)
    else:
        for j in range(i, len(n)):
            n[i], n[j] = n[j], n[i]
            perm(n, i + 1)
            n[i], n[j] = n[j], n[i]  # swap back, for the next loop


if __name__ == '__main__':
    x = [1, 2, 3, 4]
    # permutation(x, 2, len(x))
    perm(x, 0)

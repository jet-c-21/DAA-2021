"""
Given a sequence of n distinct numbers a1, a2, ..., an,
we define a significant inversion to be a pair i < j such that ai > 2aj .
Give an O(n log n) algorithm to count the number of significant inversions
in the given sequence of n distinct numbers a1, a2, ..., an.

Example:
    Input: arr[] = {1, 20, 6, 4, 5}
    Output: 3
    Significant inversion pair are (20, 6), (20, 5) and (20, 4).
"""


def count_and_merge(ls1: list, ls2: list, pairs: list):
    result = list()
    recheck = list()

    print(ls1, ls2, end=' -> ')

    while len(ls1) or len(ls2):
        if len(ls1) == 0:
            result.append(ls2.pop(0))

        elif len(ls2) == 0:
            result.append(ls1.pop(0))

        else:

            if ls1[0] > ls2[0]:
                # record significant inverse pairs

                if ls1[0] > 2 * ls2[0]:
                    print('add pairs: ', end='')
                    for larger_el in ls1:
                        for rc_el in recheck:
                            print((larger_el, rc_el), end=', ')
                            pairs.append((larger_el, rc_el))

                        pairs.append((larger_el, ls2[0]))
                    print('-> ', end='')

                else:
                    recheck.append(ls2[0])

                result.append(ls2.pop(0))

            else:
                # ls1[0] <= ls[0]
                result.append(ls1.pop(0))

    print(result)
    return result


def divide(ls: list, pairs: list):
    if len(ls) <= 1:
        return ls

    mid = len(ls) // 2

    return count_and_merge(divide(ls[0:mid], pairs),
                           divide(ls[mid:len(ls)], pairs),
                           pairs)


def get_sig_inversion(ls: list):
    if len(ls) == 0:
        return list()

    pairs = list()

    sorted_ls = divide(ls, pairs)

    return pairs, sorted_ls


if __name__ == '__main__':
    X = [1, 20, 6, 21, 5, 7, 3]
    pairs, sls = get_sig_inversion(X)
    print(pairs, len(pairs))

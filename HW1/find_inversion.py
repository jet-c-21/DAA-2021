def get_inversion_n2(ls: list):
    result = list()
    for i in range(len(ls) - 1):
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                result.append((ls[i], ls[j]))

    return result


def count_and_merge(ls1: list, ls2: list, pairs: list):
    result = list()
    recheck = 0

    print(ls1, ls2, end=' -> ')

    while len(ls1) or len(ls2):
        if len(ls1) == 0:
            result.append(ls2.pop(0))

        elif len(ls2) == 0:
            result.append(ls1.pop(0))

        else:
            if ls1[0] > ls2[0]:
                print('add pairs: ', end='')
                for el in ls1:
                    print((el, ls2[0]), end=', ')
                    pairs.append((el, ls2[0]))

                print('-> ', end='')
                result.append(ls2.pop(0))

            else:
                recheck += 1
                result.append(ls1.pop(0))

    print(result)
    return result


def divide(ls: list, si_pairs: list):
    if len(ls) <= 1:
        return ls

    mid = len(ls) // 2

    return count_and_merge(divide(ls[0:mid], si_pairs),
                           divide(ls[mid:len(ls)], si_pairs),
                           si_pairs)


def get_inversion(ls: list):
    if len(ls) == 0:
        return list()

    pairs = list()

    divide(ls, pairs)

    return pairs


if __name__ == '__main__':
    X = [1, 20, 6, 21, 5, 7, 3]
    y = get_inversion(X)
    print(len(y))

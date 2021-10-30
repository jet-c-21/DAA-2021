def merge(ls1: list, ls2: list):
    result = list()
    # print(ls1, ls2)

    while len(ls1) or len(ls2):
        if len(ls1) == 0:
            result.append(ls2.pop(0))

        elif len(ls2) == 0:
            result.append(ls1.pop(0))

        else:
            if ls1[0] < ls2[0]:
                result.append(ls1.pop(0))
            else:
                result.append(ls2.pop(0))

    return result


def merge_sort(ls: list):
    if len(ls) <= 1:
        return ls

    mid = len(ls) // 2

    return merge(merge_sort(ls[0:mid]), merge_sort(ls[mid:len(ls)]))


# a = [1, 8, 9]
# b = [2, 7, 11, 15]
# c = merge(a, b)
# print(c)

# merge_sort([])
# x = [6, 20, 11, 27, 3, 1, 9, 8, 7]
x = [8, 2, 4, 6, 9, 7, 10, 1, 5, 3]
y = merge_sort(x)
print(y)

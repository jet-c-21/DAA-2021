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


class SignificantInversion:
    def __init__(self, ls):
        self.pairs = list()
        self.ls = ls

    def count(self):
        if len(self.ls) == 0:
            return self.pairs
        self.divide(self.ls)
        return self.pairs

    def divide(self, ls: list):
        if len(ls) <= 1:
            return ls

        mid = len(ls) // 2

        return self.count_and_merge(self.divide(ls[0:mid]),
                                    self.divide(ls[mid:len(ls)]))

    def count_and_merge(self, ls1: list, ls2: list):
        result = list()

        while len(ls1) or len(ls2):
            if len(ls1) == 0:
                result.append(ls2.pop(0))

            elif len(ls2) == 0:
                result.append(ls1.pop(0))

            else:
                if ls1[0] > ls2[0]:
                    # record significant inverse pairs
                    if ls1[0] > 2 * ls2[0]:
                        for el in ls1:
                            self.pairs.append((el, ls2[0]))

                    result.append(ls2.pop(0))

                else:
                    result.append(ls1.pop(0))

        return result


if __name__ == '__main__':
    X = [1, 20, 6, 21, 5, 7, 3]
    y = SignificantInversion(X).count()
    print(y, len(y))

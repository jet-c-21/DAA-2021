# Python3 implementation of the approach
# https://www.geeksforgeeks.org/significant-inversions-in-an-array/
# Function that sorts the input array
# and returns the number of inversions
# in the array
def merge_sort_sig_inv(arr, array_size):
    temp = [0 for i in range(array_size)]
    return _merge_sort(arr, temp, 0,
                       array_size - 1)


# Recursive function that sorts the input
# array and returns the number of
# inversions in the array
def _merge_sort(arr, temp, left, right):
    mid, inv_count = 0, 0
    if right > left:
        # Divide the array into two parts and
        # call _mergeSortAndCountInv()
        # for each of the parts
        mid = (right + left) // 2

        # Inversion count will be sum of the
        # inversions in the left-part, the right-part
        # and the number of inversions in merging
        inv_count = _merge_sort(arr, temp, left, mid)
        inv_count += _merge_sort(arr, temp,
                                 mid + 1, right)

        # Merge the two parts
        inv_count += merge(arr, temp, left,
                           mid + 1, right)
    return inv_count


# Function that merges the two sorted arrays
# and returns the inversion count in the arrays
def merge(arr, temp, left, mid, right):
    inv_count = 0

    # i is the index for the left subarray
    i = left

    # j is the index for the right subarray
    j = mid

    # k is the index for the resultant
    # merged subarray
    k = left

    # First pass to count number
    # of significant inversions
    while (i <= mid - 1) and (j <= right):
        if arr[i] > 2 * arr[j]:
            inv_count += (mid - i)
            j += 1
        else:
            i += 1

    # i is the index for the left subarray
    i = left

    # j is the index for the right subarray
    j = mid

    # k is the index for the resultant
    # merged subarray
    k = left

    # Second pass to merge the two sorted arrays
    while ((i <= mid - 1) and (j <= right)):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            temp[k] = arr[j]
            k, j = k + 1, j + 1

    # Copy the remaining elements of the left
    # subarray (if there are any) to temp
    while (i <= mid - 1):
        temp[k] = arr[i]
        i, k = i + 1, k + 1

    # Copy the remaining elements of the right
    # subarray (if there are any) to temp
    while (j <= right):
        temp[k] = arr[j]
        j, k = j + 1, k + 1

    # Copy back the merged elements to
    # the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


# This code is contributed by Mohit Kumar

if __name__ == '__main__':
    # Driver code
    arr = [1, 20, 6, 21, 5, 7, 3]
    n = len(arr)
    print(merge_sort_sig_inv(arr, n))


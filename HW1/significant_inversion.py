def divide(arr, temp, left, right):
    inv_count = 0

    if right > left:
        mid = (right + left) // 2

        left_inv = divide(arr, temp, left, mid)
        right_inv = divide(arr, temp, mid + 1, right)
        # print(left_inv, right_inv)

        whole_inv = count_and_merge(arr, temp, left, mid + 1, right)
        inv_count = left_inv + right_inv + whole_inv

    return inv_count


def count_and_merge(arr, temp, left, mid, right):
    inv_count = 0

    i = left  # i is the index for the left subarray
    j = mid  # j is the index for the right subarray

    print(arr)

    while i <= mid - 1 and j <= right:
        if arr[i] > 2 * arr[j]:
            inv_count += mid - i
            j += 1
        else:
            i += 1

    i = left
    j = mid
    k = left

    # merge two sorted array
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    """
    Copy the remaining elements of the left subarray 
    (if there are any) to temp
    """
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1

    """
    Copy the remaining elements of the right subarray 
    (if there are any) to temp
    """
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy back the merged elements to the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count


def get_sig_inversion(arr, array_size):
    temp = [0 for _ in range(array_size)]

    return divide(arr, temp, 0, array_size - 1)


if __name__ == '__main__':
    X = [1, 20, 6, 21, 5, 7, 3]
    n = len(X)
    y = get_sig_inversion(X, n)
    print(y)

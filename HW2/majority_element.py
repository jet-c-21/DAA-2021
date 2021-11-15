def get_m_el_dnc(arr: list, start_idx: int, end_idx: int):
    """
    get the majority
    :param arr:
    :param start_idx:
    :param end_idx:
    :return:
    """
    if start_idx == end_idx:
        return arr[start_idx]

    mid_idx = (end_idx - start_idx) // 2 + start_idx
    left_m_el = get_m_el_dnc(arr, start_idx, mid_idx)
    right_m_el = get_m_el_dnc(arr, mid_idx + 1, end_idx)

    if left_m_el == right_m_el:
        return left_m_el

    left_count = 0
    for i in range(start_idx, end_idx + 1):
        if arr[i] == left_m_el:
            left_count += 1

    right_count = 0
    for i in range(start_idx, end_idx + 1):
        if arr[i] == right_m_el:
            right_count += 1

    if left_count > right_count:
        return left_m_el
    else:
        return right_m_el


if __name__ == '__main__':
    x = [1, 4, 1, 2, 4, 4, 2, 6, 6, 6, 6, 7]
    print(get_m_el_dnc(x, 0, len(x) - 1))

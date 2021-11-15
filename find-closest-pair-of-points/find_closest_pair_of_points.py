import math


def get_dist(p1: tuple, p2: tuple):
    return math.sqrt(((p2[1] - p1[1]) ** 2) + ((p2[0] - p1[0]) ** 2))


def get_closest_pop_bf(points: list) -> (tuple, tuple, float):
    """
    get closest pair of points by brute force

    :param points:
    :return:
    """
    min_dist = float('inf')
    p1 = None
    p2 = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = get_dist(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                p1 = points[i]
                p2 = points[j]

    return p1, p2, min_dist


def _get_closest_pop_dnc(pts_sbx: list, pts_sby: list):
    n = len(pts_sbx)

    # >>> base case >>>
    # time complexity: 3 ^ 2 = 9
    if n <= 3:
        return get_closest_pop_bf(pts_sbx)
    # <<< base case <<<

    mid_idx = n // 2
    mid_point = pts_sbx[mid_idx]

    pts_sbx_left = pts_sbx[:mid_idx]  # time complexity: n
    pts_sbx_right = pts_sbx[mid_idx:]  # time complexity: n

    # >>>>>>>>>>>>
    # time complexity: n
    pts_sby_left = list()
    pts_sby_right = list()
    for point in pts_sby:
        pts_sby_right.append(point) if point[0] > mid_point[0] else pts_sby_left.append(point)
    # <<<<<<<<<<<<

    p1_left, p2_left, delta_left = _get_closest_pop_dnc(pts_sbx_left, pts_sby_left)  # time complexity: T(n/2)
    p1_right, p2_right, delta_right = _get_closest_pop_dnc(pts_sbx_right, pts_sby_right)  # time complexity: T(n/2)

    if delta_left < delta_right:
        p1, p2, delta = p1_left, p2_left, delta_left
    else:
        p1, p2, delta = p1_right, p2_right, delta_right

    # >>> check points around split boundary >>>

    # >>>>>>>>>>>>
    # time complexity: n
    pts_in_recheck_area = list()
    for point in pts_sby:
        if mid_point[0] - delta < point[1] < mid_point[1] + delta:
            pts_in_recheck_area.append(point)
    # <<<<<<<<<<<<

    # >>>>>>>>>>>>
    # time complexity: 6n
    for i in range(len(pts_in_recheck_area)):
        for j in range(i + 1, min(i + 7, len(pts_in_recheck_area))):
            dist = get_dist(pts_in_recheck_area[i], pts_in_recheck_area[j])
            if dist < delta:
                print(f"update in recheck-area: {pts_in_recheck_area[i]}, {pts_in_recheck_area[j]}")
                p1, p2, delta = pts_in_recheck_area[i], pts_in_recheck_area[j], dist
    # <<<<<<<<<<<<

    # <<< check points around split boundary <<<

    return p1, p2, delta


def get_closest_pop_dnc(points: list):
    """
    get closest pair of points by divide and conquer

    :param points:
    :return:
    """
    pts_sorted_by_x = sorted(points, key=lambda p: p[0])
    pts_sorted_by_y = sorted(points, key=lambda p: p[1])

    return _get_closest_pop_dnc(pts_sorted_by_x, pts_sorted_by_y)


if __name__ == '__main__':
    import random

    random.seed(777)


    def gen_points(n=100, x_min=0, x_max=100, y_min=0, y_max=100, repeat=False):
        if repeat:
            return [(random.randint(x_min, x_max), random.randint(y_min, y_max)) for _ in range(n)]
        else:
            points = list()
            while len(points) != n:
                new_p = (random.randint(x_min, x_max), random.randint(y_min, y_max))
                if new_p not in points:
                    points.append(new_p)

            return points


    pts = gen_points()
    # print(pts)

    print(get_closest_pop_dnc(pts))

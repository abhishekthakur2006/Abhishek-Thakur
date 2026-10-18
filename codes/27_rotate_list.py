def rotate_list(items, k):
    if not items:
        return []

    length = len(items)
    shift = k % length

    if shift == 0:
        return list(items)

    if k >= 0:
        return items[-shift:] + items[:-shift]

    left_shift = (-k) % length
    return items[left_shift:] + items[:left_shift]

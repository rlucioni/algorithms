import random


def mergesort(unsorted):
    print('Sorting {}'.format(unsorted))

    if len(unsorted) > 1:
        midpoint = len(unsorted) // 2
        left, right = unsorted[:midpoint], unsorted[midpoint:]

        return merge(mergesort(left), mergesort(right))

    return unsorted


def merge(left, right):
    print('Merging {} and {}'.format(left, right))

    merged = []
    while True:
        if len(left) == 0:
            merged += right
            break
        elif len(right) == 0:
            merged += left
            break

        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged


if __name__ == '__main__':
    l = mergesort([random.randint(1, 100) for _ in range(10)])
    print(l)

import random


def quicksort(unsorted):
    print(f'Sorting {unsorted}')

    if len(unsorted) > 1:
        pivot = partition(unsorted)
        left, right = unsorted[:pivot], unsorted[pivot:]
        return quicksort(left) + quicksort(right)

    return unsorted


def partition(target):
    left = 0
    pivot = len(target) - 1

    while left < pivot:
        print(f'Partitioning {target}, pivoting on {target[pivot]} and comparing with {target[left]}')

        if target[left] > target[pivot]:
            target[pivot - 1], target[pivot] = target[pivot], target[pivot - 1]

            if pivot - 1 != left:
                target[left], target[pivot] = target[pivot], target[left]

            pivot -= 1
        else:
            left += 1

    return pivot


if __name__ == '__main__':
    target = [random.randint(1, 100) for _ in range(10)]
    l = quicksort(target)

    print(l)

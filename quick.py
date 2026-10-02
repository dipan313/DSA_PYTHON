lis = [9,5,6,1,2,8,7]

high = len(lis)-1
low = 0

def partition(lis, low, high):

    pivot = lis[low]

    i = low
    j = high

    while i < j:

        while lis[i] <= pivot and i < high:
            i += 1

        while lis[j] >= pivot and j >= low+1:
            j -= 1

        if i < j:
            lis[i], lis[j] = lis[j], lis[i]

    lis[low], lis[j] = lis[j], lis[low]

    return j


def quick(lis, low, high):

    if low < high:

        part = partition(lis, low, high)

        quick(lis, low, part-1)
        quick(lis, part+1, high)


quick(lis, low, high)

print(lis)
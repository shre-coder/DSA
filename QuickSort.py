def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x <= pivot]
        greater = [x for x in list1[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


l1 = [58, 62, 91, 43, 29, 37, 88, 72, 16, 30]
l1 = quick_sort(l1)
print(l1)

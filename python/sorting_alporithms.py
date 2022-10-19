def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        key = lst[i]
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


ins_s = [12, 33, 1, 34, 22, 11]
sorted_ins_s = sorted(ins_s)
print(sorted_ins_s == insertion_sort(ins_s))


def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        max_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[max_index]:
                max_index = j
        if max_index != i:
            lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst


sel_s = [99, 33, 132, 11, 1, -11, 2134, 12, 114, -1]
sorted_sel_s = sorted(sel_s)
print(sorted_sel_s == selection_sort(sel_s))


#

def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


#

bb_s = [123, 41, 24, 411142, 2, 4, -1, 12, 11, 132, 11, 1, -11, 21]
sorted_bb_s = sorted(bb_s)
#
print(sorted_bb_s == bubble_sort(bb_s))
   
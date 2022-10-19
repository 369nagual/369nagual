def selection_sort(list):
    for i in range(0, len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    return list


m_list = [34, 3, 2, 11, 23, 4, 234, 123, -1, 4, 1, 234, 12, 999, 34, 1, 3, 41, 25, 412, 4, 54635, 47, 3, 47, 34]
# insertion_sort(m_list)
print(selection_sort(m_list) == sorted(m_list))
# bubble_sort(m_list)

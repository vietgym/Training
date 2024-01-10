def remove(in_list):
    result_list = []
    set_list = set()
    for item in in_list:
        if item not in set_list:
            result_list.append(item)
            set_list.add(item)
    return result_list


def get_part(in_list, n, part):
    list1 = remove(in_list)
    avg_len = len(list1) // n
    list_result = []
    start = 0
    for i in range(n):
        if i < n - 1:
            end = start + avg_len
            list_result.append(list1[start:end])
            start = end
        else:
            end = len(list1)
            list_result.append(list1[start:end])
    return list_result[part - 1]


list_part = ['1', '2', '3', '4', '5', '6', '7']
print(get_part(list_part, 3, 2))

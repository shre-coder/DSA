# def bubble_sort(data_list):
#     for r in range(1, len(data_list)):
#         for i in range(len(data_list) - r):
#             if data_list[i] > data_list[i + 1]:
#                 data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
#                 print(data_list)


def modified_bubble_sort(data_list):
    flag = False
    for r in range(1, len(data_list)):
        flag = False
        for i in range(len(data_list) - r):
            if data_list[i] > data_list[i + 1]:
                data_list[i], data_list[i + 1] = data_list[i + 1], data_list[i]
                print(data_list)
                flag = True
        if not flag:
            break


l = [34, 67, 86, 12, 25, 50]
modified_bubble_sort(l)
print(l)

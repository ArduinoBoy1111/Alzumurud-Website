test = [4, 2, 4, 1, 5, 3, 6]


def divide(items_list):
    if len(items_list) > 1:
        count = len(items_list)
        list1 = items_list[: count // 2]
        list2 = items_list[count // 2 :]
        print(f"list1 {list1} , list2 {list2}")
        divide(list1)
        divide(list2)

    else:
        pass


divide(test)
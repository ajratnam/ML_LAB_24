def get_list(num: int) -> list[int]:
    """
    Get a list from the user

    Parameters
    ----------
    num: int
        The number of the list

    Returns
    -------
    list
        The list entered by the user
    """
    lst = input(f"Please enter list {num} - ").split()
    return list(map(int, lst))


def get_common(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    Get the common elements in two lists

    Parameters
    ----------
    lst1: list
    lst2: list
        The two lists to find the common elements in

    Returns
    -------
    list
        The common elements in the two lists
    """
    return list(set(lst1) & set(lst2))


if __name__ == "__main__":
    lst1 = get_list(1)
    lst2 = get_list(2)

    common = get_common(lst1, lst2)
    print("Common elements in the lists are:", common)

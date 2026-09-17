from typing import Counter


def PrintDuplicatesInList(lst:list):
    print(f"The Original list:{lst}")
    count = Counter(lst)
    res = [num for num, freq in count.items()if freq>1]
    print(res)
    s = set()
    dup = []
    for n in lst:
        if n in s:
            dup.append(n)
        else:
            s.add(n)
    print(dup)


a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
PrintDuplicatesInList(a)
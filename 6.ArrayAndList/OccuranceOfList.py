from typing import Counter


def occouranceOfElements(lst,n):
    count = 0
    for val in lst:
        if val == n:
            count+= 1
    print(f"The Count of {n} in list {lst}: {count}")
    print(f"The Count of {n} in list {lst}: {lst.count(n)}")
    print(f"The Count of {n} in list {lst}: {Counter(lst)}")

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
occouranceOfElements(a,3)
    
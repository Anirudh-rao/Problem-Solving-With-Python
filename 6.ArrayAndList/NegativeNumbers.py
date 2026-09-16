def NegativenNumbers(lst):
    result = []
    for i in lst:
        if i < 0:
            result.append(i)
    print(f"The Original List :{lst}")
    print(f"The Negative Numbers in list:{result}")
    n = [num for num in lst if num < 0]
    print(f"The Negative Numbers in list using list comphrehension:{n}")
    m = list(filter(lambda x: x < 0, lst))
    print(f"The Negative Nunbers in list using List Comprehension:{m}")

a = [5, -3, 7, -1, 2, -9, 4]
NegativenNumbers(a)

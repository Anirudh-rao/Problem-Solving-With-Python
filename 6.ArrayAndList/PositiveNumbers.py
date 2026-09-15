def PositveNumbers(lst):
    res = []
    for i in lst:
        if i > 0:
            res.append(i)
    print(f'original list :{lst}')
    print(f"The Positive Numbers:{res}")
    rs = [i for i in lst if i > 0]
    print(f"The Positive Numbers After list comprehension:{res}")
    flt = filter(lambda x:x>0,lst)
    print(f"The Positive Numbers using lambda:{list(flt)}")


a = [-10, 15, 0, 20, -5, 30, -2] 
PositveNumbers(a)
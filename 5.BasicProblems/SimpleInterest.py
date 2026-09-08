def simpleinterest(p,t,r):
    SI = (p*t*r)/ 100
    return SI

si = lambda p,t,r:(p*t*r) / 100
p, t, r = 8, 6, 8

res = si(p, t, r)
print(res)
print(simpleinterest(10,2,4))
print(simpleinterest(11,1,3))
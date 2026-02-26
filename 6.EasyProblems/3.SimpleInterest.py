def simpleInterest(P,T,R):
    SI = (P*T*R) / 100
    print("The Simple Interest is:",SI)
    si = lambda P,T,R : (P*T*R) / 100
    res = si(P,T,R)
    print("The Simple Interest is:",res)
    si = [P * T * R / 100][0]
    print(si)


simpleInterest(10,10,11)
simpleInterest(12,13,11)



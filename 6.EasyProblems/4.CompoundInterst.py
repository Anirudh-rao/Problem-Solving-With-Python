def compoundInterest(p,r,t):
    A = p*(1+ r/100)**t
    CI = A - p
    print("The Compound Interest:",CI)
    Amt = p * (pow((1 + r / 100), t))
    CI = Amt - p
    print("The Compound Interest with Pow Function",CI)
    Amt = p
    for i in range(t):
        Amt = Amt * (1 + r / 100)
    CI = Amt - p
    print("The Compound Interest with For Loop ",CI)



p = int(input("Principal amount: "))
r = int(input("Rate of interest: "))
t = int(input("Time in years: "))

compoundInterest(p,t,r)

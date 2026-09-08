def CompoundInterest(P,T,R):
    CompoundInterest = P * (1+ R/100)**T
    return CompoundInterest


def CompoundInterestWithPOW(P,T,R):
    Amt = P * (pow((1 + R / 100), R))
    CI = Amt - P  
    return CompoundInterest

print("Compound interest:", CompoundInterest(1200,5.4,2))
print("Compound interest wit POW:", CompoundInterestWithPOW(1200,5.4,2))
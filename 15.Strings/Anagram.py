def isAnagram(self, s: str, t: str) -> bool:
    #Method One : HashMap
    # Check if lenght are same
    if len(s) != len(t):
        return False
    
    countS, countT = {},{}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[s[i]] = 1 + countT.get(s[i],0)
    
    for c in countS:
        if countS[c] != counT[c]:
            return False
        


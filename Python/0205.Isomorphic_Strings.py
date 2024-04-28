class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return RuntimeError("Error, string must be of equal length.")
        maping_st, maping_ts = {}, {}
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            
            if ((ch1 in maping_st and maping_st[ch1] != ch2) or
                (ch2 in maping_ts and maping_ts[ch2] != ch1)):
                return False
        
            maping_st[ch1] = ch2
            maping_ts[ch2] = ch1
        return True
    
        # single line implmentation
        # retrun len(set(zip(s,t))) == len(set(s)) == len(set(t))

if __name__ == '__main__':
    x = Solution()
    print(x.isIsomorphic('foo', 'bar'))
    print(x.isIsomorphic('too', 'food'))
    print(x.isIsomorphic('paper', 'title'))
class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check if the lengths of the two strings are different
        if len(s) != len(t):
            # if they are not the same length, raise a RuntimeError
            return RuntimeError("Error, string must be of equal length.")
        
        # create two dictionaries to store mappings from characters in s to t and vice versa
        maping_st, maping_ts = {}, {}
        
        # iterate through the characters of both strings simultaneously
        for i in range(len(s)):
            # assign current characters from s and t to variables
            ch1, ch2 = s[i], t[i]
            
            # check if the current character in s has been mapped already and if the mapping is consistent
            if ((ch1 in maping_st and maping_st[ch1] != ch2) or \
                (ch2 in maping_ts and maping_ts[ch2] != ch1)):
                # if the mapping is inconsistent, return False
                return False
            
            # create a mapping from character in s to character in t
            maping_st[ch1] = ch2
            
            # create a mapping from character in t to character in s
            maping_ts[ch2] = ch1
        
        # if all characters can be consistently mapped, return True
        return True
    
        # single line implmentation
        # retrun len(set(zip(s,t))) == len(set(s)) == len(set(t))

if __name__ == '__main__':
    x = Solution()
    print(x.isIsomorphic('foo', 'bar'))
    print(x.isIsomorphic('too', 'food'))
    print(x.isIsomorphic('paper', 'title'))
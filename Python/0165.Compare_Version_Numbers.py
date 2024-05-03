class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split version strings into lists of integers
        version1_parts, version2_parts = version1.split('.'), version2.split('.')
        # get the lengths of version parts lists
        v1_len, v2_len = len(version1_parts), len(version2_parts)
        # initialize pointers for iterating through version parts
        i = j = 0
        
        # iterate through corresponding version parts and compare them
        while i < v1_len and j < v2_len:
            # convert version parts to integers for comparison
            n1, n2 = int(version1_parts[i]), int(version2_parts[j])
            # compare version parts
            if n1 > n2:
                return 1
            if n1 < n2:
                return -1
            # move to the next version parts
            i += 1
            j += 1
        
        # if there are remaining version parts in version1, check if they are non-zero
        while i < v1_len:
            n1 = int(version1_parts[i])
            if n1 > 0:
                return 1
            i += 1
        
        # if there are remaining version parts in version2, check if they are non-zero
        while j < v2_len:
            n2 = int(version2_parts[j])
            if n2 > 0:
                return -1
            j += 1
        
        # if no non-zero differences found, versions are equal
        return 0

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("1.01", "1.001"))
    print(s.compareVersion("1.0", "1.0.0"))
    print(s.compareVersion("0.1", "1.1"))
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # get the number of books
        n = len(books)
        # initialize a list to store the minimum height of shelves up to each book index
        min_height = [0] * (n + 1)
        
        # iterate through each book
        for i in range(1, n + 1):
            # get the width and height of the current book
            width, height = books[i - 1]
            # calculate the minimum height if we place the current book on a new shelf
            min_height[i] = min_height[i - 1] + height
            
            # try placing the current book with previous books to form a new shelf
            j = i - 1
            while j > 0 and width + books[j - 1][0] <= shelfWidth:
                # accumulate the width and update the height to the maximum of current 
                # and previous book heights
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                
                # update the minimum height if the current configuration is better
                min_height[i] = min(min_height[i], min_height[j - 1] + height)
                # move to the previous book to check if it can be included in the current shelf
                j -= 1
        
        # return the minimum height required to store all books
        return min_height[n]

if __name__ == '__main__':
    s = Solution()
    print(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
    print(s.minHeightShelves([[1,3],[2,4],[3,2]], 6))
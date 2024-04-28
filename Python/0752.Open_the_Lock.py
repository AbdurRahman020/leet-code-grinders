from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        dead_ends_set = set(deadends)
        queue = deque()
        queue.append(('0000', 0))
        visited = set('0000')

        while queue:
            curr_str, curr_steps = queue.popleft()

            if curr_str == target:
                return curr_steps

            if curr_str in dead_ends_set:
                continue
            
            for i in range(4):
                digit = int(curr_str[i])
                for j in [1, -1]:
                    new_digit = (digit + j) % 10
                    new_str = curr_str[:i] + str(new_digit) + curr_str[i+1:]
                    if new_str not in visited:
                        visited.add(new_str)
                        queue.append((new_str, curr_steps+1))
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
    print(s.openLock(["8888"], "0009"))
    print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
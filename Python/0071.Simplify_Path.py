class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []

        for directory in directories:
            if directory == '..' and stack:
                stack.pop()
            elif directory not in ['', '.', '..']:
                stack.append(directory)

        return '/' + '/'.join(stack)


if __name__ == '__main__':
    s = Solution()

    print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/home//foo/"))
    print(s.simplifyPath("/home/user/Documents/../Pictures"))
    print(s.simplifyPath("/../"))
    print(s.simplifyPath("/.../a/../b/c/../d/./"))

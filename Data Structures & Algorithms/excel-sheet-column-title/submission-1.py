class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        title = deque()
        while columnNumber > 0:

            offset = (columnNumber - 1) % 26
            title.appendleft(chr(ord('A') + offset))
            columnNumber = (columnNumber - 1) // 26

        return "".join(title)
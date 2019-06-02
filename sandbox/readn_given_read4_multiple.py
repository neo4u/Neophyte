"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def __init__(self):
        self.temp = [""] * 4
        self.ptr = 0
        self.count = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0

        while n:
            if self.count == 0:
                self.count = read4(self.temp)

            if self.count == 0:
                break

            while n and self.count:
                buf[i] = self.temp[self.ptr]
                self.ptr += 1
                self.count -= 1
                i += 1
                n -= 1

            if self.count == 0:
                self.ptr = 0

        return i
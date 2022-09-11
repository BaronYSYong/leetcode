"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y < 2**31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?

The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        time: 28 ms
        """
        return bin(x^y).count("1")
        
        
    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        time: 36 ms
        """        
        z = x ^ y
        count = 0
        while z > 0:
            count += z & 1
            z >>= 1
            
        return count

if __name__ == '__main__':
    h = Solution()
    print h.hammingDistance1(7,20)
    print h.hammingDistance2(7,20)

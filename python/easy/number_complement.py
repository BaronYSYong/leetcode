"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0
"""

import math

class Solution(object):
    def findComplement1(self, num):
        """
        :type num: int
        :rtype: int
        time: 36 ms (using NOT and AND)
        """
        return ~num & int('1'*(len(bin(num))-2),2)

    def findComplement2(self, num):
        """
        :type num: int
        :rtype: int
        time: 32 ms (using XOR)
        """
        return num ^ int('1'*(len(bin(num))-2),2)

    def findComplement3(self, num):
        """
        :type num: int
        :rtype: int
        time: 32 ms (Flip bit by bit)
        """
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

    def findComplement4(self, num):
        """
        :type num: int
        :rtype: int
        time: 38 ms (Find the bit length (say L) and flip num by num ^ 11...1 (L ones).)
        """
        return num ^ ((1<<num.bit_length())-1)
        
    def findComplement5(self, num):
        """
        :type num: int
        :rtype: int
        time: 36ms (Find the bit length first)
        """
        return num ^ ((1 << len(bin(num)) - 2) - 1)

    def findComplement6(self, num):
        """
        :type num: int
        :rtype: int
        time: 32 ms (using math.log)
        """
        return num ^ ((2<<int(math.log(num, 2)))-1)

"""
Given a string, you need to reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word 
order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

class Solution(object):
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str        
        time: 92 ms
        """
        word_list = s.split(" ")
        output = word_list[0][::-1]
        for i in range(1, len(word_list)):
            output += " " + word_list[i][::-1]
        return output
        
    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        time: 35 ms
        """
        return ' '.join(s[::-1].split()[::-1])

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution()
    print solution.reverseWords2(s)

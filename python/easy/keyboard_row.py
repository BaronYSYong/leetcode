"""
Given a List of words, return the words that can be typed using letters 
of alphabet on only one row's of American keyboard like the image below.

American keyboard

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""

class Solution(object):
    def findWords1(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        time: 35 ms
        """
        row1 = "QWERTYUIOPqwertyuiop"
        row2 = "ASDFGHJKLasdfghjkl"
        row3 = "ZXCVBNMzxcvbnm"
        ret = []
        for i in words:
            # Subset or equal
            if set(i) <= set(row1) or set(i) <= set(row2) or set(i) <= set(row3):
                ret.append(i)
        return ret

    def findWords2(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        time: 38 ms
        """
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and for the multiples of five output "Buzz". 
For numbers which are multiples of both three and five output "FizzBuzz".

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
""" 

class Solution(object):
    def fizzBuzz1(self, n):
        """
        :type n: int
        :rtype: List[str]
        time: 69 ms
        """
        output = [] 
        for i in range(1, n+1):
            words = ""
            if i%3 == 0:
                words += "Fizz"
            if i%5 == 0:
                words += "Buzz"
            if words == "":
                words += str(i)
            output.append(words)
        return output
    
    def fizzBuzz2(self, n):
        """
        :type n: int
        :rtype: List[str]
        time: 76 ms
        """    
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

    def fizzBuzz3(self, n):
        """
        :type n: int
        :rtype: List[str]
        time: 69 ms
        """    
        return['FizzBuzz'[i%-3&-4:i%-5&8^12]or`i`for i in range(1,n+1)]
        
    def fizzBuzz4(self, n):
        """
        :type n: int
        :rtype: List[str]
        time: 105 ms
        """
        return [str(i) * (i % 3 != 0 and i % 5 != 0) + "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) 
        for i in range(1, n + 1)]    

if __name__ == '__main__':
    n = 15
    output = Solution()
    for i in output.fizzBuzz4(n):
        print i
    
    

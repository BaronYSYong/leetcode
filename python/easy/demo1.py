"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

For another example, given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3], the function should return 1.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [-1,000,000..1,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
"""

def solution(A):
    A.sort()
    num = 0
    count = 0
    if len(A) == 1 and A[0] > 0:
		if A[0] > 1:
			return 1
		else:
			return 2
    
    for i in range(len(A)-1):
        if A[i] > 0:            
            if count == 0 and A[i] > 1:
                return 1			
            if A[i+1] - A[i] > 1:
                return A[i]+1
            if i == len(A)-2:
                return A[i+1]+1
            count +=1
    return num+1

print solution([1, 3, 6, 4, 1, 2])


"""
Analysis
Detected time complexity:
O(N) or O(N * log(N))
"""

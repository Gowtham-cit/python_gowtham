"""
https://leetcode.com/problems/valid-perfect-square
"""
#solution
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num ** 0.5 == int(num**0.5): return True

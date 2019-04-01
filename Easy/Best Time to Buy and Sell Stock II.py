'''Best Time to Buy and Sell Stock II
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''


class Solution:
    def re(prices, i):
        if len(prices[i:]) > 2:
            ind = diff(prices[i], prices[i:])
            mx, mx_ind = re(prices, i+1)
            if ind < mx_ind-1:
                return prices[ind]-prices[i] + mx, ind
            else:
                return max((prices[ind]-prices[i], ind), mx, mx_ind)
            
            
            # return max((prices[ind]-prices[i], ind), re(prices, i+1))
        else:
            return max((0, -1), (prices[i+1]-prices[i], i+1))
        
    def diff(num, sub):
        mx = 0
        mx_ind = -1
        sz = len(sub)
        for i in range(1, sz):
            (mx, mx_ind) = (sub[i] - num, i) if (sub[i] - num > mx) else (mx, mx_ind)
        return mx_ind
    
    def maxProfit(self, prices: List[int]) -> int:
        mx, = re(prices, 0)
        return mx
        
    
                
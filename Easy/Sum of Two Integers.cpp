/*
https://leetcode.com/problems/sum-of-two-integers/

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
*/

class Solution {
public:
	int getSum(int a, int b) {
		unsigned int c = a^b;
		unsigned int d = a&b;
		unsigned int e = d << 1;
		
		
		while(d){
			e = d << 1;
			d = c & e;
			c = c ^ e;
		}
		return c;
	}
};
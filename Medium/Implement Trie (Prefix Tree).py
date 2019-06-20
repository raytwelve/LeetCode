'''
https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

'''

class Trie:
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		# tup = (isWord, suffix)
		# suffix[ch1] -> suffix[ch2] -> suffix[ch3] -> ...
		
		self.root = (False, dict())

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		tup = self.root
		d = None
		for i in range(len(word)):
			d = tup[1]
			ch = word[i]
			tup = d.setdefault(ch, (False, dict()))
		d[word[-1]] = (True, tup[1])
		

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		tup = self.root
		for i in range(len(word)):
			d = tup[1]
			ch = word[i]
			if ch not in d.keys(): return False
			tup = d[ch]
		return tup[0]

	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		tup = self.root
		for i in range(len(prefix)):
			d = tup[1]
			ch = prefix[i]
			if ch not in d.keys(): return False
			tup = d[ch]
		return True
		

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
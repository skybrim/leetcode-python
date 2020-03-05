# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: Wiley<throughskybrim@gmail.com>
"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

"""


class TrieNode:
    """
    Trie Node.
    """
    def __init__(self):
        """
        Initialize node.
        """
        self.is_end = False
        self.nodes = [None for _ in range(26)]

    def contains_key(self, char):
        """
        Returns if char in node.
        """
        return self.nodes[ord(char) - ord('a')] is not None

    def get(self, char):
        """
        Return node by char
        """
        return self.nodes[ord(char) - ord('a')]

    def put(self, char, node):
        """
        Insert new node into nodes.
        """
        self.nodes[ord(char) - ord('a')] = node

    def set_end(self):
        """
        Set is_end True.
        """
        self.is_end = True


class Trie:
    """
    Trie.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if not node.contains_key(char):
                node.put(char, TrieNode())
            node = node.get(char)
        node.set_end()

    def search_prefix(self, word):
        """
        Returns node the prefix end.
        """
        node = self.root
        for char in word:
            if node.contains_key(char):
                node = node.get(char)
            else:
                return None
        return node

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.search_prefix(word)
        return node is not None and node.is_end is True

    def start_with(self, prefix):
        """
        Returns if there is any word in the trie that starts
        with the given prefix.
        """
        node = self.search_prefix(prefix)
        return node is not None


if __name__ == "__main__":
    TRIE = Trie()
    TRIE.insert("apple")
    print(TRIE.search('apple'))
    print(TRIE.search('app'))
    print(TRIE.start_with('app'))
    TRIE.insert('app')
    print(TRIE.search('app'))

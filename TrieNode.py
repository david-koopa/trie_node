class TrieNode:
        def __init__(self):
            self.child = [None] * 26
            self.word_end = False

def insert(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            new_node = TrieNode()
            curr.child[index] = new_node
        curr = curr.child[index]
    curr.word_end = True

def search_key(root, key):
    curr = root
    for c in key:
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False
        curr = curr.child[index]
    return curr.word_end

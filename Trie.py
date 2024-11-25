class Trie:
    def __init__(self):
        self.child = {}
        self.terminal = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = Trie()
            curr = curr.child[c]
        curr.terminal = True

    def find_next_possible_letter(self, phrase):
        curr = self
        for c in phrase:
            if c not in curr.child:
                return ''
            curr = curr.child[c]
        return curr.child.keys()

    def auto_complete_next_word(self, phrase):
        curr = self
        next_word = phrase + ''

        # traverse to part of phrase
        for c in phrase:
            if c not in curr.child:
                return 'word not found'
            curr = curr.child[c]

        # combine rest of word based on first letters
        while not curr.terminal:
            next_letter = list(curr.child.keys())[0]
            next_word += next_letter
            curr = curr.child[next_letter]
        return next_word

if __name__ == '__main__':
    t = Trie()
    t.insert('add')
    print(t.find_next_possible_letter('a'))

    t.insert('adore')
    print(t.find_next_possible_letter('ad'))

    phrase = 'ado'
    print(f'next word for {phrase}: {t.auto_complete_next_word(phrase)}')
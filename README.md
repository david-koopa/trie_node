### Basic Usage

Data structure for dynamic set of strings.

Construct a Trie and add the word 'ant'.
```
from TrieNode import *
t = TrieNode()
t.insert(t, 'ant')
t.insert(t, 'adore')
```

The word 'ant' exists, because we added it earlier. 
```
print(search_key(t, 'ant') == True) #True
```

The word 'and' doesn't exist.
```
print(search_key(t, 'and') == False) #True
```

Suggest next word (unoptimized).
```

phrase = 'ado'
print(f'next word for {phrase}: {t.auto_complete_next_word(phrase)}')
```
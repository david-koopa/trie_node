### Basic Usage

Data structure for dynamic set of strings.

Construct a Trie and add the word 'ant'.
```
from TrieNode import *
t = TrieNode()
insert(t, 'ant')
```

The word 'ant' exists, because we added it earlier. 
```
print(search_key(t, 'ant') == True) #True
```

The word 'and' doesn't exist.
```
print(search_key(t, 'and') == False) #True
```

# Hash
Python implementation: `hash_table = {}`
Argument: `key: value`

## Complexity
### Create
Time: O(N) / Space: O(N)
### Insert/Delete/Search
Time: O(1) - avg, O(N) - worst (hash collidion) / Space: O(1)
Take a note, that hash table has to read input (key) first, and then it will do search in O(1) time. That's why, true search with hash table is in O(K) Time, where K - size of input.
### Nuances
O(N) time takes memory resizing of cache once we exceed its limit (like a dynamic array), for that, we do O(N) hashing.

## Some code
```
table = {1: 2}
table[5] = 4
for key in table:
    print(key)
for value in table.values():
    print(value)
```

## Usage
Great to use when you need fast search/insert/delete in data massive.
There is no order in hash table, but you can add additional attribute as `'index'` to assign it. Or to create LinkedList style by creating `'next_node'`.
Nice to use when need to count letters in strings, search if second string contains permutations of first one and so one in different variosity.

# String
Python implementation: `word = 'some_string'` or to convert `str(10)`
Strings are immutable in py.

## Complexity
### Create
Time: O(N) / Space: O(N)
### Insert/Delete
We create brand new string once we insert or delete any letter there.
Time: O(N) / Space: O(N)
###Search
Time: O(k) (k - index of letter) / Space: O(1)

## Some code
```
sentence = 'Just be a ranger in your soul'
splitted_sentence = sentence.split(' ')  # create list of words
symbol = '%20'
print(symbol.join(splitted_sentence))  # insert symbol between words

print(sentence.find('be'))  # find first appearance of 'be',
                            # if there is no, then return -1
```

## Algorithms for strings
### Unique letters
There are huge variety of tasks to compare letters in strings. Hash table are used widely for such topics:
- Find duplicates in a string.
- Compare uniques of strings.
### Edits in strings
- How many edits needs to perform to get same anagrama of string2 from string1? Example(https://github.com/kotsky/programming-exercises/blob/master/String/One%20Edit%20Or%20Less.py)
  - Some anagramma tasks can be solved by sort all strings into alphabet order.
- Find min number of operation to be done to get string2 from string1. DP method. Example(https://github.com/kotsky/programming-exercises/blob/master/Dynamic%20Programming/Min%20Number%20Of%20Edits.py)

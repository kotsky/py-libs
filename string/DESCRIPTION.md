# String
Python implementation: `word = 'some_string'` or to convert int `10` to string is `str(10)`.
Strings are immutable in py.

## Complexity
### Create
Time: O(N) / Space: O(N)
### Insert/Delete
We create brand new string once we insert or delete any letter there.
Time: O(N) / Space: O(N)
### Search
Time: O(k) (k - index of letter) / Space: O(1)

## Some code
```
sentence = 'Just be a ranger in your soul'
splitted_sentence = sentence.split(' ')  # create list of words
symbol = '%20'
  
# splitted_sentence has to contain only string for .join method
print(symbol.join(splitted_sentence))  # insert symbol between strings

print(sentence.find('be'))  # find first appearance of 'be',
                            # if there is no, then return -1
```

## Algorithms for strings
Hold in your mind follows:
- Hash tables can be your friends in problems of unique letters.
- 2 pointers to check letters from different indexes.
- Prefix and suffix - how you can use them to solve your problem?
- Use tries data structure in problems of searching/matching + prefix /suffix.
- Majority of usage is Ascii table.

### Number conversion
- [Roman to Integer](https://github.com/kotsky/programming-exercises/edit/master/String/Roman%20To%20Integer.py): create LUT for pattern searching. If there is no respective number in LUT, then we deal with new part of the number.

### Search in string

#### [Knuth Morris Pratt Algorithm](https://github.com/kotsky/py-libs/blob/master/string/knuth_morris_pratt.py)
Find if `substring` is in `string` in O(M + N) Time and O(M) space, where M is length of substring, and N is length of string.

#### Aho-Corasick Algorithm	[TBD]
Find if `substring` is in `vocablary`, where `vocablary = [string_one, string_two, ...]` in O(M + N + Z) Time / ??? Space.

### Unique letters
There are huge variety of tasks to compare letters in strings. Hash table are used widely for such topics:
- Find duplicates in a string.
- Compare uniques of strings.
- [Smallest Substring Containing](https://github.com/kotsky/programming-exercises/blob/master/String/Smallest%20Substring%20Containing.py) - to find the smallest range in a big string, which contains all symbols of a small string. Here we use hash table to track symbols and 2 pointers for range adjustments ("window" method).

### Edits in strings
- How many edits needs to perform to get same anagrama of string2 from string1? [One Edit Or Less](https://github.com/kotsky/programming-exercises/blob/master/String/One%20Edit%20Or%20Less.py)
  - Some anagramma tasks can be solved by sort all strings into alphabet order.
- Find min number of operation to be done to get string2 from string1. DP method. [Min Number Of Edits](https://github.com/kotsky/programming-exercises/blob/master/Dynamic%20Programming/Min%20Number%20Of%20Edits.py)

### Compression	/ Matching
Main idea here is often to split string, and then to build back with certain modification using .join method.
- Convert 'Have a power in your soul' into 'Have%20a%20power%20in%20your%20soul'.
- Compress sequence of same letters into shorter format like 'aaabb' to 'a3b2'. [Word Compression](https://github.com/kotsky/programming-exercises/blob/master/String/Word%20Compression.py)

#### [Patter Match](https://github.com/kotsky/programming-exercises/blob/master/String/Pattern%20Matcher.py)
Here we try to replace certain substrings with predeterminded patterns like `"xxyxxy", "gogopowerrangergogopowerranger" => [x, y] = ["go", "powerranger"]`. Here, we split string onto letters and store it in arrays, and then with pure math we calculate if it's possible to have that pattern for `y` if we have that range size of `x`.

Another example of patterns might be to find out special key word in a string, and to mark it with a special symbol like `_`. 
Example: [Underscorify Substring](https://github.com/kotsky/programming-exercises/blob/master/String/Underscorify%20Substring.py): `['test is in testest this'], 'test' => '_test_ is in _testest_ this'`.
To solve this, simply find each appearance of the special word in the string, merge intervals if needed and create new string.

### Rotation
- [String Rotation](https://github.com/kotsky/programming-exercises/blob/master/String/String%20Rotation.py) - Check if string2 contains preffix of string1. And then check other letters per origin order.

### Palindromes
Palindrome - a string which reads the same backwards.
To check, is string is a palindrome, traverse with 2 pointers from the start and from the end and check if these letters are equivalent.

In case you need to find the [longest palindrome is string](https://github.com/kotsky/programming-exercises/blob/master/String/Longest%20Palindromic%20Substring.py), go through string and at each index explore in 2 directions if that substring is a palindome.

### Permutation
Permutation - when you can change order of string. To solve those problems, Unique Letters topic comes to play.
- [Find all permutation](https://github.com/kotsky/programming-exercises/blob/master/String/Find%20All%20Permutation.py)

### Anagrams
If you need to work with anagrams like `['flop', 'olfp']`, then you might want at first sort strings in alphabet order, and then compare strings and check, if they are anagrams.
- [Group Anagrams](https://github.com/kotsky/programming-exercises/blob/master/String/Group%20Anagrams.py)






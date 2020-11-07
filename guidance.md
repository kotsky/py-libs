# Python 3 Style Rules

Refer to https://google.github.io/styleguide/pyguide.html
## Naming
`module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`.

## up to 80 chr in a line
Of course, there might be some exception.
```
x = ('This will build a very long long \
long long long long long long string')

a = ('This will build a very long long '
     'long long long long long long string')
```
```
      # See details at
      # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
```

## With as
```  
Yes:  with very_long_first_expression_function() as spam, \
           very_long_second_expression_function() as beans, \
           third_thing() as eggs:
          place_order(eggs, beans, spam, beans)
No:  with VeryLongFirstExpressionFunction() as spam, \
          VeryLongSecondExpressionFunction() as beans:
       PlaceOrder(eggs, beans, spam, beans)
Yes:  with very_long_first_expression_function() as spam:
          with very_long_second_expression_function() as beans:
              place_order(beans, spam)
```
## Indentation

```
       # Aligned with opening delimiter
       foo = long_function_name(var_one, var_two,
                                var_three, var_four)
       meal = (spam,
               beans)

       # Aligned with opening delimiter in a dictionary
       foo = {
           long_dictionary_key: value1 +
                                value2,
           ...
       }

       # 4-space hanging indent; nothing on first line
       foo = long_function_name(
           var_one, var_two, var_three,
           var_four)
       meal = (
           spam,
           beans)

       # 4-space hanging indent in a dictionary
       foo = {
           long_dictionary_key:
               long_dictionary_value,
           ...
       }
```

## Coma Trailing
```
golomb3 = [0, 1, 3]
golomb4 = [
   0,
   1,
   4,
   6,
]

dictionary = {
  'foo'      : 1,
  'long_name': 2,
}
```
## Code structures
### Modules
```
"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""
```

### Functions and Methods
```
def fetch_smalltable_rows(table_handle: smalltable.Table,
                          keys: Sequence[Union[bytes, str]],
                          require_all_keys: bool = False,
) -> Mapping[bytes, Tuple[str]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: Optional; If require_all_keys is True only
          rows with values set for all keys will be returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```
#### Several more examples:
After annotating, many function signatures will become “one parameter per line”.
```
def my_method(self,
              first_var: int,
              second_var: Foo,
              third_var: Optional[Bar]) -> int:
  ...
```
Always prefer breaking between variables, and not, for example, between variable names and type annotations. However, if everything fits on the same line, go for it.
```
def my_method(self, first_var: int) -> int:
  ...
```
If the combination of the function name, the last parameter, and the return type is too long, indent by 4 in a new line.
```
def my_method(
    self, first_var: int) -> Tuple[MyLongType1, MyLongType1]:
  ...
```
### Classes
Classes should have a docstring below the class definition describing the class. If your class has public attributes, they should be documented here in an Attributes section and follow the same formatting as a function’s Args section.
```
class SampleClass:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```
### Strings
```
Yes:
  Python('Why are you hiding your eyes?')
  Gollum("I'm scared of lint errors.")
  Narrator('"Good!" thought a happy Python reviewer.')
```
```
  long_string = """This is fine if your use case can accept
      extraneous leading spaces."""
   
  long_string = ("And this too is fine if you cannot accept\n"
                 "extraneous leading spaces.")
```

## Main
In Python, pydoc as well as unit tests require modules to be importable. If a file is meant to be used as an executable, its main functionality should be in a main() function, and your code should always check if __name__ == '__main__' before executing your main program, so that it is not executed when the module is imported.

Use absl to build app from Python -> https://github.com/abseil/abseil-py
When using absl, use app.run:
```
from absl import app
...

def main(argv):
    # process non-flag arguments
    ...

if __name__ == '__main__':
    app.run(main)
```
Otherwise, use:
```
def main():
    ...

if __name__ == '__main__':
    main()
```
All code at the top level will be executed when the module is imported. Be careful not to call functions, create objects, or perform other operations that should not be executed when the file is being pydoced.

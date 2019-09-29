Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myList = [2,3,4]
>>> len(myList)
3
>>> for i in myList:
	print(i)

	
2
3
4
>>> myList[2]
4
>>> myList
[2, 3, 4]
>>> print(myList)
[2, 3, 4]
>>> myList.append(5)
>>> myList
[2, 3, 4, 5]
>>> for i in myList:
	print(i)

	
2
3
4
5
>>> lang = ['python'. 'c#'. 'c++', 'javascript', 'html', 'css' ]
SyntaxError: invalid syntax
>>> >>> lang = [ 'python'. 'c#'. 'c++', 'javascript', 'html', 'css' ]
SyntaxError: invalid syntax
>>> lang = [ 'python'. 'c#'. 'c++', 'javascript', 'html', 'css' ]
SyntaxError: invalid syntax
>>> lang = [ 'python', 'c#', 'c++', 'javascript', 'html', 'css' ]
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> help()list
SyntaxError: invalid syntax
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> lang.insert(0, "java")
>>> lang
['java', 'python', 'c#', 'c++', 'javascript', 'html', 'css']
>>> lang.remove("html")
>>> lang.append("sql")
>>> lang
['java', 'python', 'c#', 'c++', 'javascript', 'css', 'sql']
>>> lang.print(upper("python"))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    lang.print(upper("python"))
AttributeError: 'list' object has no attribute 'print'
>>> for 1 in lang:
	print(upper(1))
	
SyntaxError: can't assign to literal
>>> for 1 in lang:
	print(1)
	
SyntaxError: can't assign to literal
>>> for i in lang:
	print(1)

	
1
1
1
1
1
1
1
>>> print(lang)
['java', 'python', 'c#', 'c++', 'javascript', 'css', 'sql']
>>> print(lang[1])
python
>>> capitalize(lang)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    capitalize(lang)
NameError: name 'capitalize' is not defined
>>> capitalize(lang, /)
SyntaxError: invalid syntax
>>> upper(lang)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    upper(lang)
NameError: name 'upper' is not defined
>>> lang.upper
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    lang.upper
AttributeError: 'list' object has no attribute 'upper'
>>> print(lang.upper)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(lang.upper)
AttributeError: 'list' object has no attribute 'upper'
>>> print(lang.upper())
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(lang.upper())
AttributeError: 'list' object has no attribute 'upper'
>>> upper = lang.upper()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    upper = lang.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> p = "python"
>>> print(p.uppep)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(p.uppep)
AttributeError: 'str' object has no attribute 'uppep'
>>> upperP = p.upper()
>>> print(upperP)
PYTHON
>>> print( lang[1].upper() )
PYTHON
>>> myDictionary = {'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary['index2']
2
>>> myDictionary['index3']
355
>>> dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '111-222-3333'} }
>>> print(dic_users['em_1235'])
{'fname': 'Mary', 'lname': 'Jones', 'phone': '111-222-3333'}
>>> print(dic_users['em_1235']['phone'])
111-222-3333
>>> print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'], dic_users['em_1235']['lname'], dic_users['em_1235']['phone']))
User: Mary Jones
Phone: 111-222-3333
>>> answer = True
>>> type(answer)
<class 'bool'>
>>> answer = False
>>> type(answer)
<class 'bool'>
>>> progName = "Python"
>>> answer = "I love {}!".format(progName)
>>> print(answer)
I love Python!
>>> i = 0
>>> for i in range(10):
	print("() iteration through the loop.".formst(i))
	i += 1

	
Traceback (most recent call last):
  File "<pyshell#76>", line 2, in <module>
    print("() iteration through the loop.".formst(i))
AttributeError: 'str' object has no attribute 'formst'
>>> for i in range(10):
	print("{} iteration through the loop.".formst(i))
	i += 1

	
Traceback (most recent call last):
  File "<pyshell#78>", line 2, in <module>
    print("{} iteration through the loop.".formst(i))
AttributeError: 'str' object has no attribute 'formst'
>>> for i in range(10):
	print("{} iteration through the loop.".format(i))
	i += 1

	
0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.
>>> while i < 10:
	print("{} iteration through the loop.".format(i))
	i += 1

	
>>> i = 0
>>> while i < 10:
	print("{} iteration through the loop.".format(i))
	i += 1

	
0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is equal to 12
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is GREATER than to 12
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is EQUAL to 12 and they have the key
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is EQUAL to 12 and they DO NOT have the key
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is GREATER than to 12
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_if.py 
num1 is LESS than 12
>>> myList = ('Pink','Black','Green','Teal','Red','Blue')
>>> for color in myList:
	if color == 'Black':
		print('the vhosen color is green')

		
the vhosen color is green
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
red
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 

>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
red
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
I like the color red
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
Traceback (most recent call last):
  File "C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py", line 9, in <module>
    color_function()
  File "C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py", line 7, in color_function
    print("{} {}".format(mySentence,color_list[i]))
TypeError: list indices must be integers or slices, not str
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
I like the color red
I like the color blue
I like the color green
I like the color pink
I like the color teal
I like the color black
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
TYLER loves the color red
TYLER loves the color blue
TYLER loves the color green
TYLER loves the color pink
TYLER loves the color teal
TYLER loves the color black
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
TYLER loves the color red
TYLER loves the color blue
TYLER loves the color green
TYLER loves the color pink
TYLER loves the color teal
TYLER loves the color black
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
TYLER loves the color red
TYLER loves the color blue
TYLER loves the color green
TYLER loves the color pink
TYLER loves the color teal
TYLER loves the color black
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
TYLER loves the color red
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
['TYLER loves the color red']
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
['TYLER loves the color red', 'TYLER loves the color blue', 'TYLER loves the color green', 'TYLER loves the color pink', 'TYLER loves the color teal', 'TYLER loves the color black']
>>> 
 RESTART: C:/Users/Tyler/Desktop/The-Tech-Academy-Basic-Python-Projects/Python_functions.py 
TYLER loves the color red
TYLER loves the color blue
TYLER loves the color green
TYLER loves the color pink
TYLER loves the color teal
TYLER loves the color black
>>> fName = input("What is your first name?")
What is your first name?
>>> fName = input("What is your first name? ")
What is your first name? 
>>> fName = input("What is your first name?\n")
What is your first name?

>>> 

>>> fName = input("What is your first name?\n>>>")
What is your first name?
>>>
>>> fName = input("What is your first name?\n>>> ")
What is your first name?
>>> 

>>> 
>>> fName = input("What is your first name?\n>>> ")
What is your first name?
>>> 
>>> Tyler
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    Tyler
NameError: name 'Tyler' is not defined
>>> fName = input("What is your first name?\n>>> ")
What is your first name?
>>> Tyler
>>> fname
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    fname
NameError: name 'fname' is not defined
>>> fName
'Tyler'
>>> lName = input("What is your last name?\n>>> ")
What is your last name?
>>> Lyons
>>> fname
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    fname
NameError: name 'fname' is not defined
>>> fName
'Tyler'
>>> lName
'Lyons'
>>> 

>>> print("Hello {} {}, Welcome to Python!".format(fName,lName))
Hello Tyler Lyons, Welcome to Python!
>>> 

"""
As the re.match documentation says:
===================================
If zero or more characters at the beginning of string match the regular expression pattern,
return a corresponding MatchObject instance. Return None if the string does not match the pattern;
 note that this is different from a zero-length match.

Note: If you want to locate a match anywhere in string, use search() instead.

re.search searches the entire string, as the documentation says:
===============================================================
Scan through string looking for a location where the regular expression pattern produces a match,
 and return a corresponding MatchObject instance. Return None if no position in the string matches the pattern;
 note that this is different from finding a zero-length match at some point in the string.

So if you need to match at the beginning of the string, or to match the entire string use match. It is faster.
 Otherwise use search.

The documentation has a specific section for match vs. search that also covers multiline strings:

Python offers two different primitive operations based on regular expressions: match checks for a match only at
the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).

"""
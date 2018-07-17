# Regular Expression: powerful tool for various string manipulation
# They are a domain specific language (DSL) in python and other programming languages
# DSL are specilaized small program language
# Using regular expression we can
#  - veriy that strings match pattern ( eg: format of email address *@*.*)
#  - perform substitution in string

# In Python the regular expression is addressed using re module.
# re - is part of standard library

# After defining regular expression, the re.match function
# can be used to determine whether it matchs at the begining of a string

# if re.match() returns an object representing the match if match exists
# if re.match() returns None if match does NOT exists

# using r"expression" => means experssion use raw string
# Raw string don't escape anything, this is easier to work with re.

import re

pattern = r"hello"

if re.match(pattern,"Hello, world"):
    print ("pattern matchs with Hello, world")
else:
    print ("no match")
    
if re.match(pattern,"hello!, world"):
    print ("pattern matches with hello!,world")
else:
    print ("no match")

# re.search function finds a match of pattern anywhere in the string
# re.findall returns a list of all substring that match a pattern
# re.finditer does the same thing as re.findall, except this return iterator
#  rather than a list

import re

pattern = r"r?d"

if (re.search(pattern,"red god bad rod")):
    print ("pattern matched to string - r?d exists")
else:
    print ("pattern r?d doesn't match")
pattern = r"red"
print("example findall")
print(re.findall(pattern,"red god bad rod"))
    
#################### NOTE : more functions of re ####################

# The regex search returns an object with several method that give details about it.
# Includes
#   - group method - returns the string matched.
#   - start and end - returns the start and ending position of the first match
#   - span - returns start and end positons of the first match as tuple.

import re

pattern = r"hello"

match= re.search(pattern,"hello world hello python")
if match:
    print (match.group())
    print (match.start())
    print (match.end())
    print (match.span())

###################### IMPORTANT : sub method in re ####################
# Most important re method that uses regex is sub

# Syntax
#             re.sub(pattern,repl,string, max=0)

# replace all occurances of the  pattern in with string repl.
# unless max provided

import re

str1 ="Dude hello! first hello world program"

pattern=r"hello"
newStr = re.sub(pattern,"Tom",str1)
print(newStr)

###################### IMPORTANT : Metacharacters ##################
# Metacharacters are more useful to create regular expression more generic
# for example to represent concept like 'one or more repitation of a vowel'

# The existence of metacharaters causes problem, because it needs to be escaped
# may on or more time.

# in order to cutout the usage of multiple backslash for escaping character,
# we can use r (raw string) like r"expression"

str =r"this is \r\a\w string"

# 1. Metacharacter . (dot or period)
# which means it matches any character other than new line.

import re

pattern = r"r.d"

if re.match(pattern,"red"):
    print("pattern matchs red")


if re.match(pattern,"rad"):
    print("pattern matchs rad")

if re.match(pattern,"r2d"):
    print("pattern matchs r2d")

# 2. Metacharacter ^ and $
# ^ = start of the string
# $ = end of a string 

import re

pattern = r"^gr.y$"

if re.match(pattern,"grey"):
    print("match1")

if re.match(pattern, "stringgray"):
    print("Match2")

############ IMPORTANT : Character classes ######################
# Character classes provide a way to match only one of a specific
# set of characters

# A character class is created by putting the characters it matches
# inside square brackets.

import re

pattern = r"[aeiou]"

if re.search(pattern,"hello"):
    print("vowel exists")

if re.search(pattern,"rhym by"):
    print("vowel exists")

# NOTE: The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.

# Character classes - can also match ranges of character

# class [a-z] matches any lowercase alphbetic character
# class [G-P] matches any uppercase character from G to P
# class [0-9] matches any digit

import re

pattern =r"[0-9][A-Z][a-z]"

if re.search(pattern,"9Dx"):
    print("matching pattern 1")

if re.search(pattern,"D9a"):
    print ("matching pattern not 2")

# NOTE: placing ^ at the start of a character class to *invert* it
# This causes it to match any character other than the ones included
# other metacharacters such as $ and . have not meaning within character class
# The metacharacter ^ has no meaning unless it is the first character in a class

import re

pattern = r"[^A-Z]" # excludes upper case strings due to ^

if re.search (pattern,"all lower case"):
    print("match all lower case")
    

# NOTE : More metacharacters
# *  - means "Zero or more repititions of the previous thing"
# It tries to match as many repititions as possible.
# The previous thing can be a single character, a class or a group of char in paranthesis
# + - means "one or more repititions of previous thing
# ? - means zero or one repititions"
# { } - curly braces used to represent the number of repetition between numbers
# All the above metacharacters specify number of repetitions

import re
# *
pattern =r"(hel)*lo"

if re.match(pattern,"helhello"):
    print(">>>>>match1")
    
if re.match(pattern,"helhelhelhello"):
    print(">>>>>match2")

# +

pattern = r"g+"

if re.match(pattern,"ggggggggg"):
    print("matched g+ pattern")

if re.match(pattern,"ad"):
    print("ad pattern??")

# NOTE:
# * matches 0 or more occurrences of the preceding expression.
# + matches 1 or more occurrence of the preceding expression.

# ?
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "ice--cream"): # not matches
   print("Match 2")

# {} => {x,y} - means between x and y repetition of something
# {0,1} is more like ?
# if first number is missing it is considered as 0,
# if second number missing it is considered as infinity

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("9match 1")

if re.match(pattern,"9999"):
    print ("match9999")

if re.match(pattern,"999"):
    print ("match999")

# Groups - can be created by surrounding part of a re with parantheses
# This means that a group can be given as an argument to metacharacter such as * and ?

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match egg 1")
if re.match(pattern, "eggspspe"):
   print("Match eggspe 1")

# Groups -> group() function can be used to access the content of a match
# A call of group(0) or group() returns the whole match. 
# A call of group(n), where n is greater than 0, returns the nth group from the left. 
# The method groups() returns all groups up from 1.

import re

pattern =r"a(bc)(de)(f(g)h)i"

match = re.match(pattern,"abcdefghijklmnopqrstuvwxyz")

if match:
    print(match.group()) # compelete expression
    print(match.group(0)) # compelete expression
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

# NOTE : Special groups:
# 1. named groups
# 2. non-capturing groups

# Named groups have the format (?P<name>...),
# where name is the name of the group, and ... is the content.
# They behave exactly the same as normal groups, except they can
# be accessed by group(name) in addition to its number.

# Non-capturing groups have the format (?:...).
# They are not accessible by the group method, so they can
# be added to an existing regular expression without breaking the numbering.

import re

pattern = r"(?P<first>abc)(?:def)(ghi)" #?: will not consider it to be within the group

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first")) # first - name provided in the group
   print(match.groups()) # ?: is not part of the output

# quiz : What would be the result of len(match.groups()) of a match of (a)(b(?:c)(d)(?:e))?
# ans 3

# | - metacharacter represents or
# This means "or", so red|blue matches either "red" or "blue"

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match gray")

match = re.match(pattern, "grey")
if match:
   print ("Match grey")
   
match = re.match(pattern, "griy")
if match:
    print ("Match 3")

############### IMPORTANT : Special sequences #####################
# There are various special sequences that can use regular expressions.
# They are written using backslash followed by another character.
# 1. special sequence is backslash followed by number between 1 -99
# example \1 or \23 => this matches the expression of the group of that number.


import re

pattern = r"(.+) \1" # note the space between ) \
# + means 1 to many
match = re.match(pattern, "word word")
#print ("{}{}".format(match,pattern))
if match:
   print ("Match 1 special sequences")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2 special sequences")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3 special sequences")

# Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression,
# which is the matched expression itself, and not the regex pattern.

# \d => digits
# \s => whitespaces
# \w => word character

# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
# In Unicode mode they match certain other characters, as well.
# For instance, \w matches letters with accents.

# Special sequences with upper case letters - \D, \S, and \W
# - mean the opposite to the lower-case versions.
# For instance, \D matches anything that isn't a digit.

import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1 - special \D")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2 - special \D")

match = re.match(pattern, " ! $?") # only _ is applicabe \D
if match:
    print("Match 3 - special \D")

match = re.match(pattern, "_ 123") # only _ is applicabe \D (not digit)
if match:
    print("Match 3 - special \D")

# Additional special sequences are \A, \Z, and \b.
# The sequences \A and \Z match the beginning and end of a string, respectively. 
# The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.

import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1 >> \A\Z\B")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2 >> \A\Z\B")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3 >> \A\Z\B")

# EMAIL EXTRACTION FROM STRING

str = "Reply to info@domain.com for updates"

# we need to identigy info@domain.com
pattern =r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

match = re.search(pattern, str)
if match:
   print(match.group())

# In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses



















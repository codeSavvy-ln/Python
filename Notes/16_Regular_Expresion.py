"""
The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) The letters set the corresponding flags defined below.
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
"""

"""
import re
help(re)
"""

#findall - returns the matching value
#search - returns the match object if it satisfies the pattern
#split - returns a list where the string has been split at each match
#sub - replaces one or many matches with a string

"""
\s --> Space character
\S --> except space character
\d --> any digit
\D --> ecept digit
\w --> any word character (alpha numeric character [a-zA-z0-9]
\W --> Any character except word (special characters [^a-zA-Z0-9]
.  --> Every character
[] --> A set of character "[a-m]"
\  --> Signals a special sequence (can also be used to escape special characters) "\d"
^  --> starts with "^hello"
$  --> Ends with "world$"
*  --> Zero or more occurrences "aix*"
+  --> One or more occurrences "aix+"
{} --> Exactly the specified number of occurrences "al{2}"
|  --> Either or "falls|stays"

"""
import re

txt = "This is sample program where you can list of words in this text"
x = re.findall("\S+",txt)
y = re.search("\s",txt)
z = re.split("\s",txt)
g = re.sub("\s","11",txt)
print(x)
print(y)
print(z)
print(g)
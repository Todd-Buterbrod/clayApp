import re

s = "11111_a"
d = "999Я@"
regex = r'^[a-z0-9_]{1,24}$'
pattern = re.compile(regex)
if re.match(pattern,s):
    print("Matched:", s)
if re.match(pattern,d):
    print("Matched:", d)
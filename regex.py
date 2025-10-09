# regEx regular expression
# for what: search, validation, split, sub
import re

re.search #search substr in str
re.match #search substr in str
re.sub #
re.split
re.findall

res=re.findall(r"[aeiou]+", "vsadlchöaskjchöaschöaKJHCY") #['e', 'o', 'o']
print(res)
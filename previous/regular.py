import re

html = "frodo"
regular = "fro[a-z]{2}"

p = re.compile(regular)

m = p.match(html)

print(bool(m))
#print(re.compile("[a-z]+").findall("hong tae ha"))
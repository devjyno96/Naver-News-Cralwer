import re

t = re.compile(r'\d\d\d\d.\d\d.\d\d')

sibal_test = "F.E타임스"
test = "2010.11.11"

print(t.search(sibal_test))

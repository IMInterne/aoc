import re;i=int;r=re.compile(r"(\w+)-(\w+) (\w): (\w+)")
for s in (lambda o:i(o[0])<=o[3].count(o[2])<=i(o[1]),lambda o:(o[3][i(o[0])-1]==o[2])!=(o[3][i(o[1])-1]==o[2])):
  with open('i') as f: print(sum(s(r.match(l).groups())for l in f))
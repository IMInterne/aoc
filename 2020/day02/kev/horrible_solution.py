import re

strategy_map = {
    "count": lambda o: int(o['lindex']) <= o['password'].count(o['letter']) <= int(o['rindex']),
    "position": lambda o: (o.password[int(o['lindex'])-1] == o['letter']) != (o['password'][o['rindex']-1] == o['letter'])
}

# 2-4 r: prrmspx
regex = re.compile(r"(?P<lindex>\d+)-(?P<rindex>\d+) (?P<letter>\w): (?P<password>\w+)")
if __name__ == '__main__':
    is_valid = strategy_map["count"]
    with open('input.txt') as f:
        print(sum(is_valid(regex.match(line).groupdict()) for line in f))

# https://www.hackerrank.com/challenges/compress-the-string/problem

import re
print(*[(len(i), int(i[:1])) for i in re.split(r"(?<=(.))(?!\1)",input())[::2]])

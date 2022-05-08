import io
import sys

_INPUT = """\
6
. . . .
. o o .
. x x .
. . . .
o o x x
o o x x
x x o o
x x o o
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  c=[list(input().split()) for _ in range(4)]
  for i in reversed(range(4)):
    print(*c[i][::-1])
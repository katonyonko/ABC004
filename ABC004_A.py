import io
import sys

_INPUT = """\
6
1000
1000000
0
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(2*N)
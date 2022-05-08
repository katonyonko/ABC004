import io
import sys

_INPUT = """\
6
1
5
22
100000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  ans=[]
  for i in range(6):
    if i==N%5:
      ans.append(N//5%6+1)
    elif i<N%5:
      ans.append((N//5%6+1+i)%6+1)
    else:
      ans.append((N//5%6+i)%6+1)
  print(*ans,sep='')
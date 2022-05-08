import io
import sys

_INPUT = """\
6
2 3 4
17 2 34
267 294 165
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  R,G,B=map(int,input().split())
  def c(s,p,k):
    if s>=p:
      return k*(2*s-2*p+k-1)//2
    elif s+k-1<=p:
      return k*(2*p-2*s-k+1)//2
    else:
      return (p-s)*(p-s+1)//2+(s+k-1-p)*(s+k-p)//2
  ans=10**20
  for i in range(-799,-99):
    for j in range(i+R,max(i+R,0)+1):
      ans=min(ans,c(i,-100,R)+c(j,0,G)+(c(100-(B-1)//2,100,B) if j+G<=100-(B-1)//2 else c(j+G,100,B)))
  print(ans)
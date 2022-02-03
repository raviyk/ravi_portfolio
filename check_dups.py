n = len(A)
ans = 0
for i in range(n):
  ans = ans ^ A[i]
return ans

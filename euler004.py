i=999
maxpal=1

def isPalindrome(n):
  strN = str(n)
  revN = strN[::-1]
  if strN == revN:
    return True
  else:
    return False

while i>100:
  j=1000
  while j>= i:
    j-=1
    if isPalindrome(i*j):
	  maxpal = max(i*j,maxpal)
  i-=1

print maxpal
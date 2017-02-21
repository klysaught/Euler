sum=0
i=1
lim=1000

while i < lim:
  if i%3==0 or i%5==0:
    sum+=i
  i+=1
print sum
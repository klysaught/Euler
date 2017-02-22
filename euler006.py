sumn=0
sqsum=0

for n in xrange(101):
  sumn = sumn+n
  sqsum = sqsum+pow(n,2)

print pow(sumn,2)-sqsum

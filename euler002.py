sum=0
fibout=4000000

fibs=[1,2]

def next_fib():
  global fibs
  fibs.append(fibs[-1]+fibs[-2])

while fibs[-1] < fibout:
  next_fib()

del fibs[-1]

for fib in fibs:
  if fib%2==0:
    sum+=fib
	
print sum


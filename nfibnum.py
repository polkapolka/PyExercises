def nfibnum( num ):
...  a=0
...  b=1
...  for i in range(0, num):
...   fib = a +b
...   a = b
...   b = fib
...  return fib

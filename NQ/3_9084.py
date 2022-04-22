
a = [1, 5, 7]

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

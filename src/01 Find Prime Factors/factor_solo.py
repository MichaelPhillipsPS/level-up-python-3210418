def check_prime(refnum):
  isprime = True

  for num in range(2, int(refnum ** 0.5) + 1):
    if refnum % num == 0:
      isprime = False
      break
  
  return isprime

def get_prime_factors(refnum):
  if check_prime(refnum) == True:
    return refnum

  factorlist = []
  primelist = []
  primefactorlist = []

  for num in range(2, int(refnum / 2) + 1):
    if refnum % num == 0:
      factorlist.append(num)

  for factor in factorlist:
    if check_prime(factor) == True:
      primelist.append(factor)

  primelist.sort(reverse = True)
  while check_prime(refnum) == False:
    for prime in primelist:
      if refnum % prime == 0:
        primefactorlist.append(prime)
        refnum = refnum / prime
  
  primefactorlist.append(int(refnum))
  primefactorlist.sort()
  return primefactorlist

get_prime_factors(630)
get_prime_factors(100)
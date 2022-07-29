

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

print("Numeros primos")
l = 1
primo = False
while l <= 50:
  primo = is_prime(l)
  if primo:
    print(l)
  l+=1




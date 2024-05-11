def daraja(a, b):
  if b == 0:
    return 1
  elif b < 0:
    return 1 / daraja(a, -b)
  else:
    return a * daraja(a, b - 1)
print(daraja(2,4))
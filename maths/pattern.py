k=0
prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,
59,61,67,71,73,79,83,89,97,101,103,107,109,113]
for i in range(1,102400):
  if not all([bool(i%j) for j in prime]):continue
  c=0
  k+=1
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      c=1
      break
  if c==0:
    print('█',end='')
  elif c==1:
    print(' ',end='')
  # if i%20==20:
  #   print(',\n',end='')
  #   print('{:6d}'.format(i), end='')


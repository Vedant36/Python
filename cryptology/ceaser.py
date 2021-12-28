as0='''
dfsd scsxc
'''
asd=as0[1:-1]
print(f'{list(asd)}')

# shift=-5
qwe=[]
for shift in range(0,26):
  qwe=[]
  for i in asd:
    if ord(i) in range(97,97+26):
      qwe.append(chr((ord(i)+shift)%26+97))
    else: qwe.append(i)

  print(''.join(qwe))

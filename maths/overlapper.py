
'''answer
def nonovl(l, idx, right, ll):
    if idx == len(l):
        if ll:
            print(ll)
        return

    next = idx + 1  
    while next < len(l) and right > l[next][0]:
        next += 1
    nonovl(l, next, right, ll)

    next = idx + 1
    right = l[idx][1]
    while next < len(l) and right > l[next][0]:
        next += 1
    nonovl(l, next, right, ll + str(l[idx]))
(6.0, 7.25)
(2.5, 4.5)
(2.5, 4.5)(6.0, 7.25)
(2.0, 5.75)
(2.0, 5.75)(6.0, 7.25)
(2.0, 4.0)
(2.0, 4.0)(6.0, 7.25)
(0.0, 4.0)
(0.0, 4.0)(6.0, 7.25)
(0.0, 2.0)
(0.0, 2.0)(6.0, 7.25)
(0.0, 2.0)(2.5, 4.5)
(0.0, 2.0)(2.5, 4.5)(6.0, 7.25)
(0.0, 2.0)(2.0, 5.75)
(0.0, 2.0)(2.0, 5.75)(6.0, 7.25)
(0.0, 2.0)(2.0, 4.0)
(0.0, 2.0)(2.0, 4.0)(6.0, 7.25)
'''

import numpy as np

x = np.sort(np.array([(0.0, 2.0), (0.0, 4.0), (2.5, 4.5), (2.0, 5.75), (2.0, 4.0), (6.0, 7.25)]), axis=0)

def over(x):
  ret = list()
  ned = x[:,0]
  for i in x:
    tmp = i
    for j in ned[np.where(ned==i[1])[0][0]:]:
      pass
  return ret

print(x)
print(x[:,0])
# print(over(x))

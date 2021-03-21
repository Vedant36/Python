
import numpy as np

def frob_gen(*nums):
  a = np.arange(nums[0])
  for i in nums[1:]:
    pass
  return np.unique(a)

asd = frob_gen(3,5)
print(asd)

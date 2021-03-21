import numpy as np
import matplotlib.pyplot as plt

# Number of times simulation is run
n = 100000
# Array to store number of gold to get at least 12 enderpearls
arr = np.zeros((n))

for i in range(n):
	pearls = 0
	used_gold = 0
	while pearls<12:
		used_gold+=1
		if np.random.randint(459)<10:	pearls+=np.random.randint(2,5)
	arr[i] = used_gold

# # Get occurences as a function of number of gold
num_gold, occurences = np.unique(arr, return_counts=1)
# # Scale down occurences by number of times the simulation was run
probablity = occurences/n
print(np.sum(num_gold*probablity))
plt.scatter(num_gold, probablity, s=1)
plt.xlabel("Number of gold")
plt.ylabel("Probablity")
plt.show()
'''
10000 - 23.7
8000 - 19.7
5000 - 12.9
3000 - 8.3
time = 0.0023 * n
'''
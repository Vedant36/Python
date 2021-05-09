import time as t
import random as r

le,rang=1000,200
qwe=[]
for i in range(le):
	qwe.append(r.randint(0,rang))
print(qwe)
class sort:

	def s0(nums):nums.sort()

	#Bubble Sort
	def s1(nums):
		a=0
		swapped = True
		while swapped:
			swapped = False
			for i in range(len(nums) - 1):
				if nums[i] > nums[i + 1]:
					nums[i], nums[i + 1] = nums[i + 1], nums[i]
					a+=1
					swapped = True
		return a

	def s2(nums):
		a=0
		for i in range(len(nums)):
			for j in range(len(nums)-1):
				if nums[j]>nums[j+1]:
					nums[j],nums[j+1]=nums[j+1],nums[j]
					a+=1
		return a

	#Selection Sort
	def s3(nums):
		a=0
		for i in range(len(nums)):
			lowest_value_index = i
			for j in range(i + 1, len(nums)):
				if nums[j] < nums[lowest_value_index]:
					lowest_value_index = j
			nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
			a+=1
		return a

	def s4(nums):
		a=0
		for i in range(len(nums)):pass
		return a

	#Insertion sort
	def s5(nums):
		a=0
		for i in range(1, len(nums)):
			item_to_insert = nums[i]
			j = i - 1
			while j >= 0 and nums[j] > item_to_insert:
				nums[j + 1] = nums[j]
				a+=1
				j -= 1
			nums[j + 1] = item_to_insert
		return a
	def s6(nums):pass

for i in range(7):
	avg=0
	for j in range(10):
		b=t.time()
		nums=list(qwe)
		swaps=eval('sort.s'+str(i)+'(nums)')
		avg+=1000*(t.time()-b)
	avg/=10
	print(avg)

'''
Notes: Fastest way to sort must be to find the shortest Hamiltonian
cycle to swap items the least number of times.
[5,3,8,1,0,4] -- [0,1,3,4,5,8]
>[0,3,8,1,5,4]
>[0,1,8,3,5,4]
>[0,1,4,3,5,8]
>[0,1,3,4,5,8]
'''

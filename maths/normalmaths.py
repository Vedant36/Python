a = [13, 17, 25, 41, 85]

prev = False
qwe = list()
why = list()
for i in range(100):
	io = True
	for j in a:
		io = io and i%j
	if io:
		why.append(i)
		if prev:
			qwe[-1][0]+=1
		else:
			qwe.append([1,i])
	prev = io
print(sorted(qwe, reverse=True)[:10])
# print(why)
# qwe=[0, 1, 2, 3, 4, 5, 6, 7, 12, 13, 15, 16, 17, 34, 35, 37, 38, 67, 83]
# i=qwe[-1]
# while i<100000:
#   i+=1
#   a = list(str(i**2))
#   if a==sorted(a):
#     qwe.append(int(int(''.join(a))**0.5))
# print(*qwe,sep=', ')

# import random
# def primesbelow(N):
# 		correction = N % 6 > 1
# 		N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
# 		sieve = [True] * (N // 3)
# 		sieve[0] = False
# 		for i in range(int(N ** .5) // 3 + 1):
# 			if sieve[i]:
# 				k = (3 * i + 1) | 1
# 				sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
# 				sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
# 		return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]
# smallprimeset = set(primesbelow(100000))
# def is_prime(n, precision=7):
# 	if n <= 3:return n >= 2
# 	elif n % 2 == 0:return False
# 	elif n < 100000:return n in smallprimeset
# 	d = n - 1
# 	s = 0
# 	while d % 2 == 0:
# 		d //= 2
# 		s += 1
# 	for repeat in range(precision):
# 		a = random.randrange(2, n - 2)
# 		x = pow(a, d, n)
# 		if x == 1 or x == n - 1: continue
# 		for r in range(s - 1):
# 			x = pow(x, 2, n)
# 			if x == 1:return False
# 			if x == n - 1:break
# 		else: return False
# 	return True
# asd = list()
# for j in range(1, 10001):
# 	def f(n):
# 		if is_prime(n):
# 			P.add(n)
# 			for d in {1, 3, 7, 9}:
# 				f(j*n + d)
# 	P = set()
# 	for n in {2, 3, 5, 7}:f(n)
# 	asd.append([len(P), j, max(P)])
# #160 as j or as 160*n+d gives big number
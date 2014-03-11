maxn = 1000000

res = [0 for i in range(maxn)]

res[1] = 1

def action(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def colliatz(n):
	if i <= 0:
		return 0
	if n < maxn and res[n] > 0:
		return res[n]
	
	return 1 + colliatz(action(n))

for i in reversed(range(maxn)):
	res[i] = colliatz(i)

print(max(((i, r) for i, r in enumerate(res)), key=lambda x : x[1]))



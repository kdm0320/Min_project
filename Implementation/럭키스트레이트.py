n = input()

mid_point = len(n)//2 -1

left = 0
right = 0

for i in range(len(n)):
	if i <= mid_point:
		left+=int(n[i])
	else:
		right += int(n[i])

if left == right:
	print("LUCKY")
else:
	print("READY")
	


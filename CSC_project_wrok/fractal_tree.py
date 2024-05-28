lst = []
for i in range(0 , 100):
    lst.append("#x")

for i in range(1, 100 + 1):
	for j in range(1 , 100 + 1 ):
		if j % i == 0:
			if lst[j-1] == "*":
				lst[j-1] = "#"
			elif lst[j-1] == "#":
				lst[j-1] = "*"

print(lst)
def celebrity(M, n):

	# Create an adjacency list for each person
	adj = [[] for i in range(n)]
	for i in range(n):
		for j in range(n):
			if M[i][j] == 1:
				adj[i].append(j)
				
	# Check if there is a person
	# who doesn't know anyone but
	# everyone knows him/her
	for i in range(n):
		if not adj[i]:
			flag = True
			for j in range(n):
				if i == j:
					continue
				if i not in adj[j]:
					flag = False
					break
			if flag:
				return i
	return -1

# Sample input
M = [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
n = len(M)
Celebrity = celebrity(M, n)
if Celebrity != -1:
	print("Celebrity is : ", Celebrity)
else:
	print("No celebrity")
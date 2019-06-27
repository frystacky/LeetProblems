List = ["flower","flow","flight","flgenta","flowering","bob"]

def compare(x):
	output = ""
	size = 0
	if len(x) == 0:
            return output
        elif len(x) == 1:
            return x[0]
	for i in range(len(x[1])):
		if x[1][i] == x[2][i]:
			output+=str(x[1][i])
		else:
			break
	for i in range(2,len(x)):
		size = 0
		for j in range(len(output)):
			if output[j] == x[i][j]:
				size+=1
			else:
				output=output[0:size]
				size=0
				break
	return output

print(compare(List))


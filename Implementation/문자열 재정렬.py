s = input()

string = ""
number = 0

for i in s:
	if i.isalpha():
		string+=i
	else:
		number+=int(i)
		
string = "".join(sorted(string))
answer = string+str(number)
print(answer)



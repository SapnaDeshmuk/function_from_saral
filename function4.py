def check_number(num1,num2):
	if num1 and num2 %2==0:
		print"dono numbers even hai"
	else:
		print "dono numbers even nhi hai"
check_number(4,9)

def check_numbers_list(num1,num2):
	i=0
	while i<6:
		if num1[i]%2==0 and num2[i]%2==0:
			print "dono even hai"
		else:
			print "dono even nhi hai"
		i=i+1
check_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])

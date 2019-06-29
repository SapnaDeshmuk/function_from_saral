def calculator(num_x,num_y,operation):
	if operation=="add":
		print num_x+num_y
	elif operation=="subtract":
		print num_x-num_y
	elif operation=="multiply":
		print num_x*num_y
	elif operation =="divide":
		print num_x/num_y
#calculator(20,25,"add")
#calculator (40,3,"subtract")
#calculator (10,4,"multiply")
#calculator(40,4,"divide")

#number_1=calculator(20,25,"add")
#number_2=calculator (40,3,"subtract")
#number_3=calculator (10,4,"multiply")
#number_4=calculator(40,4,"divide")

#add_result=calculator(20,25,"add")
#subtract_result=calculator (40,3,"subtract")
#multiply_result=calculator (10,4,"multiply")
#divide_result=calculator(40,4,"divide")

def list_change():
	i=0
	while i<4:
		x=[5,10,50,20]
		y=[2,20,3,5]
		z=x[i]*y[i]
		print z
		i=i+1
list_change()

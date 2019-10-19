def add(x,y):
	return(x+y)
def subs(x,y):
	return x-y
def multiply(x,y):
	return(x*y)
def divide(x,y):
	return(x/y)

print("Select operation")
print("1.add ")
print("2.subs")
print("3.multiply")
print("4.divide")
choice= input("Enter 1/2/3/4 ")

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))

if choice =="1":
	print(num1,"+",num2,"=",add(num1,num2))
elif choice =="2":
	print(num1,"-",num2,"=", subs(num1,num2))
elif choice =="3":
	print(num1,"*",num2,"=", multiply(num1,num2))
elif choice =="4":
	print(num1,"/",num2,"=", divide(num1,num2))
else: 
	print("Error value,choose something else")


num= int(input("put number "))
s=0
temp=num
while temp>0:
	d=temp%10
	s+=d**3
	temp//=10
if num==s:
	print(num," yes arm")
else:
	print(num," no arm")

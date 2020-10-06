print("---------Demonstration of Array-----------");

import array as arr

a=arr.array('i',[2,4,6,8]);

print("First Element :",a[0]);
print("Second Element :",a[1]);
print("Second last element :",a[-1]);
print("");

a=arr.array('f',[2.4,4.5,6.5,8.8]);

print("First Element :",a[0]);
print("Second Element :",a[1]);
print("Second last element :",a[-1]);

print("the typecode of a is :",a.typecode)
print("");

print("Reverse of a is :");
a.reverse()
for i in range(len(a)):
	print(a[i]);

print("array of b is :")
b=arr.array('i',[1,2,1,2])
for i in range(len(b)):
	print(b[i]);

print("USe of While loop :")
i=0
while(i<len(b)):
	print(b[i]);
	i+=1;

##//////////////////////////////////////////////////////////////////////////////////////////
## OUTPUT:
##	---------Demonstration of Array-----------
##	First Element : 2
##	Second Element : 4
##	Second last element : 8
##
##	First Element : 2.4000000953674316
##	Second Element : 4.5
##	Second last element : 8.800000190734863
##	the typecode of a is : f
##
##	Reverse of a is :
##	8.800000190734863
##	6.5
##	4.5
##	2.4000000953674316
##	array of b is :
##	1
##	2
##	1
##	2
##	USe of While loop :
##	1
##	2
##	1
##	2
##//////////////////////////////////////////////////////////////////////////////////////////////////

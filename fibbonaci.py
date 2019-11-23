from time import sleep

fibb=0
a=0
b=1
for i in range(int(input("Ile liczb chcesz Mongole? "))):
	fibb=a+b
	a=fibb
	b=a-b
	print(fibb)
	sleep(0.01)
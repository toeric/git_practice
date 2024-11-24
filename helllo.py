import sys

def say_hello_world():
	print("Hello World")
	return

def say_hello_to(name):
	print("Hello " + name)
	return

def show_love(name1, name2):
	print(name1 + " loves " + name2)
	return

say_hello_world()
say_hello_to("Novem")
say_hello_to("Jocelyn")
say_hello_to("Penguin")

show_love("Novem", "Jocelyn")

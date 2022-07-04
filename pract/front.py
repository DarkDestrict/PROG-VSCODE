from cgi import print_arguments


print("Hi, Emma who is coming to your place today on your list below?\n")

list = ["Peter", "John", "Ciela", "Emma"]
print(list)
name = input("I'm not sure yet but let me check my list: ")
who_else = input("And who else is coming there: ")
print(name + " And " + who_else + " Is the ones coming today to my place.")

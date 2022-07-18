
"""
name = "The day is super good today."
print(name)

nam = input("What is your name: ")
print("My name is: " + nam)

age = 20
age += 1
print("How old are you: " + str(age))

height = float(250)
print("how high are you bro: " + str(height) + "cm")

i = "mike"
human = input("Enter human name if you are a human: ")
if i != "mike":
    print("You are a human.")

else:
    print("You are not human.")

kill = 10
me = 15
u = 80
time = 120

sum = kill != me != u != time
print(sum)

kill = 10
me = 10
u = 10
time = 10

kill == me == u == time
print(kill, me, u, time)

n = "big dog"
print(len(n))
print(type(n))
print(n.upper())
print(n.lower())
print(n.title())
print(n.count("dog"))
print(n.isdigit())
print(n.replace("dog", "Mike"))
print(n*2)

import math

pi = 3.14

a = 30
b = 100.50
c = 1000
print(max(a, b, c))
print(min(a, b, c))
print(pow(pi,2))
print(abs(pi))
print(round(b))
print(math.floor(c))
print(math.ceil(a))


m = 35
while m <= 40:
    m += 1

print(m)

print("\n")

n = 30
for i in range(30, 100):
     i += 1
     print(i)
     
print("\n")

names = ["bee", "john", "wick"]
for i in names:

    print(i)

print("\n")

name = ["lion", "hack"]
print(name.append("love"))
print(name)

print("\n")

list = ["banana", "orange", "peach"]
for fruits in list:
    print(fruits)
    if fruits == "orange":
         continue
     
print("\n")

for i in range(35, 46):
    i += 1
    print(i)
else:
    print("all done")
    
print("\n")

def cloth(name):
    name = ["killer", "Zoe", "YOU"]
    print(name)
    
join = name.append(["hacking"])
cloth(join)

print("\n")

surn = ["jain", "rose", "john", "whereis"]
nami = ["Koos", "hook", "wood", "william"]

for x in surn:
    for y in nami:
        print(x, y)
     


for x in [0, 1, 2]:
  pass


def join(ben):
    ben = input("Enter ben's number below: ")
    print("here is ben no " + ben)
    return ben


join("")

def ink(*fruits):
    print("what fruits is in your mind " + fruits[1])
    
ink("orange", "peach", "pear", "banana")
"""
print("My first project in python _name_games!!!")

score = 0

name_games = input("Enter the name of the person you think of: ")
if name_games != "age":
    print("The name " + name_games + " is not Correct!")
    score += 1
    
else:
    print("The name " + name_games + " is Correct!")
    
years = input("Enter the years you have: ")
if years == range(20, 40):
    print("The name " + years + " is not Correct!")
    score += 1
    
else:
    print("The age " + years + " is Correct!")
    
shoes = input("Enter the shoes size: ")
if shoes != 8:
    print("The shoes size  " + shoes + " is not Correct!")
    score += 1
    
else:
    print("The shoes size " + name_games + " is Correct!")
    
print("this " + str(score) + " are correct!")
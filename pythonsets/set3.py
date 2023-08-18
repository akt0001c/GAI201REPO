#1
tuple1 = [("John", 25), ("Jane", 30)]
for ls in tuple1:
  (name, age) = ls
  print(f"{name} is {age} years old")

#2
dictionary1 = {}
dictionary1["John"] = 25
print(dictionary1)
dictionary1["John"] = 26
print(dictionary1)
del dictionary1

#3
import numpy as np

arr = np.array([2, 7, 11, 15])
arr.sort()
x = 0
y = len(arr) - 1
k = 9
while (x < y):
  sum = arr[x] + arr[y]
  if (sum == k):
    print(x, y)
    break
  elif (sum > k):
    y -= 1
  else:
    x += 1

#4  Palindrome Check
s = "madam"
x = 0
y = len(s) - 1
b = False
while (x < y):
  if (s[x] != s[y]):
    print("Not a Palindrome")
    b = True
    break
  else:
    x += 1
    y -= 1

if b == False:
  print("Palindrome")

#5 selection sort
import numpy as np


def swap(x, y, arr):
  tmp = arr[x]
  arr[x] = arr[y]
  arr[y] = tmp
  return


arr = np.array([64, 25, 12, 22, 11])
lenarr = len(arr)
x = 0

while (x < lenarr - 1):
  y = x
  min = x
  while (y < lenarr):
    if (arr[y] < arr[x]):
      min = y
    y += 1

  swap(x, min, arr)
  x += 1

for i in arr:
  print(i)

#Fizz Buzz
for i in range(1, 100 + 1):
  if (i % 3 == 0 and i % 5 == 0):
    print("FizzBuzz")
  elif (i % 3 == 0):
    print("Fizz")
  elif (i % 5 == 0):
    print("Buzz")
  else:
    print(i)

#file handling

myfile = open("a.txt", "r")
wordlist = myfile.read().split()
count = len(wordlist)
print(count)
myfile.close()

str_count = str(count)
str = "Number of words : " + str_count
newfile = open("output.txt", "w")
newfile.write(str)
newfile.close()
print("file has been closed")

#exception handling using try and exception
try:
  ans = 5 / 0
  print(ans)
except ZeroDivisionError:
  print("A number cannot be divided by zero")
except:
  print("Error occured ")
else:
  print("No err occured")
finally:
  print("this is the demo of exception handling")

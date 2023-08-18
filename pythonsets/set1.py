#1
print("Helllo,World")

#2
name = "Ankit"
age = 25
active = True
h = 6.0
print(f"Type of variable 1:{type(name)},value {name}")
#3
num = [1, 4, 5, 6, 3, 7, 8, 2, 9, 10]
num.append(20)

num.remove(4)
num.sort()
print(num)

#4 sum and Average
list5 = [10, 20, 30, 40]
sum = 0
average = 0
for y in list5:
  sum = sum + y

average = sum / len(list5)
print(sum, average)


#5
def getReverseString(str):
  s = str[::-1]
  return s


ans = getReverseString("ankit")
print(ans)

#6
#program to find vowel in given string
str = "Ankit"
count = 0
vowel = "aeiouAEIOU"
for s in str:
  if (s in vowel):
    count += 1

print(count)

#7 program to find that given number is prime or not
number = 5


def checkPrime(num):
  if (num == 1 or num == 0):
    return False
  for i in range(2, num - 1):
    if (number % i == 0):
      return False
  return True


print(checkPrime(number))

#8 Fectorial Calculation


def getFectorial(num):
  if (num == 1 or num == 0):
    return 1
  return num * getFectorial(num - 1)


ans = getFectorial(5)
print(ans)

#9 Febonacci

limit = 5
list1 = [0, 1]
a = 0
b = 1
rang = limit - 2
if (rang <= 2):
  print("list :")
else:
  for i in range(1, rang + 1):
    c = a + b
    list1.append(c)
    a = b
    b = c

for j in list1:
  print(j)

#10  create list of square from 1 to 10 using list comparasion
list3 = [k**2 for k in range(1, 10 + 1)]
for x in list3:
  print(x)

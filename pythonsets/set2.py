#1 print the pattern
num = 5
for i in range(1, num + 1):
  s = ""
  for j in range(1, i + 1):
    tmp = str(j)
    s = s + tmp + " "
  print(s)

#2  interate over the list
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
  if (i % 5 == 0 and i <= 150):
    print(i)
  elif (i > 500):
    break
  else:
    continue

#3
s1 = "Ault"
s2 = "Kelly"
mid = len(s1) // 2
s3 = s1[0:mid] + s2 + s2[mid:len(s1)]
print(s3)

#4
str1 = "PyNaTive"
upper = ""
lower = ""
for char in str1:
  if (char.isupper()):
    upper = upper + char
  else:
    lower = lower + char

ans = lower + upper
print(ans)

#5
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly", "we", "lco", "me"]

list3 = []
x = 0
y = 0
len1 = len(list1)
len2 = len(list2)
while (x < len1 or y < len2):
  if (x >= len1 and y < len2):
    list3.append(list2[y])
    y += 1
  elif (y >= len2 and x < len1):
    list3.append(list1[x])
    x += 1
  else:
    s = list1[x] + list2[y]
    list3.append(s)
    x += 1
    y += 1

for z in list3:
  print(z)

#6
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

len1 = len(list1)
len2 = len(list2)
list3 = []

for x in range(0, len1):
  for y in range(0, len2):
    s = list1[x] + " " + list2[y]
    list3.append(s)

for z in list3:
  print(z)

#7
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
len1 = len(list1)
len2 = len(list2)
x = 0
y = len2 - 1
while (x < len1 and y >= 0):
  print(list1[x], list2[y])
  x += 1
  y -= 1

#8
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
ans = {}
for emp in employees:
  ans[emp] = defaults

for emp, defaults in ans.items():
  print(emp, defaults)

#9
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

ans = {}
for key in keys:
  ans[key] = sample_dict[key]

for key, value in ans.items():
  print(key, value)

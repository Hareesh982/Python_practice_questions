str1 = "Sheena loves eating mango and apple. Her sister also loves eating apple and mango"
li = str1.split()

di = {}

for i in li:
    if i not in di.keys():
        di[i] = li.count(i)
print(di)

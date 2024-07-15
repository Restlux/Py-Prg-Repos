x=open("text.txt", "r")
y=x.read()
sp=y.split()
l=""
k=0
for i in sp:
    obj=""
    for j in range(len(i)):
        if i[j].isalpha():
            obj+=" "
        elif i[j].isdigit():
            obj+=i[j]
    l+=obj+" "
sp1=l.split()
for i in sp1:
    k+=int(i)
print(k)
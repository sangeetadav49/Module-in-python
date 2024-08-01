f=open(r"c:\test\readline1.txt")
d=f.readlines()
print(d)
c=0
for i in d:
    if i[-1]=="\n" and i[-2]=='m':
        c=c+1 
    elif i[-1]=="m":
        c=c+1
print(c)

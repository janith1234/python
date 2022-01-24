f1=open("f1.txt")
f=open("f.txt")
data1=f.read()
data2=f1.read()

with open("f.txt", 'w') as a:
    a.write(data2) 
with open("f1.txt", 'w') as b:
    b.write(dat
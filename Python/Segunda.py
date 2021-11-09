""" x=[0,1,2,3,4,5,9,1]
#print(type(x))
#print(len(x))
#print(x[7:10]) """
""" if 7 in x:
    print("Si esta") """
""" x[0:4]=[1,1,1,1,1] """
""" print(x)
for i in range(len(x)-1):
    print(str(x[i]) , end=",")
print(x[len(x)-1])
print(len(x)) """

""" x.append("hola")
print(len(x))
x.insert(3," ")
y=["hola", " ", "mundo", "hp"]
x.extend(y[2:4])
print(x)
x.remove("hola")
x.remove("mundo")
x.remove("hp")
x.pop(3)
del x[1]
print(x)
[print(i) for i in x]
x.sort(reverse = True)
print(x)
 """
#diccionarios

""" x={"id":1,"nombre":"Juan"}
y={"id":2,"nombre":"Pablo"}
w=[x,y]
print(x["nombre"])
for i in w:
    print(i["nombre"]) """

#Condicionales
x=[0,1,2,3,4,5,9,1]
#x=3

while True:
    y=int(input())
    if y==1:
        print(x)
    elif y==2:
        print(y)
    elif y==3:
        print("3")
        break
    elif y==4:
        print("4")
        break
    else:
        print("default")
    u=str(input())
    if u=="no":
        break
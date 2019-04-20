import random
vector_uno=[]
vector_dos=[]
vector_suma=[]
rango=int(input("Ingrese el rango del vector"))
for i in range(rango):
    vector_uno.append(random.randint(0,20))
    vector_dos.append(random.randint(0,20))
for i in range(len(vector_uno)):
    vector_suma.append(vector_uno[i]+vector_dos[i])
print "Valores uno: ",vector_uno
print "Valores dos: ",vector_dos
print "resultado: ",vector_sumas

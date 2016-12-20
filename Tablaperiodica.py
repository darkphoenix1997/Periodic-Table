
# coding: utf-8

# In[ ]:


#Table Periodic
import csv
print "Hey sup dude"
print "Welcome to the periodic table"
print "This is a program about the actually periodic table with the 118 elements discovered, write  position of element you want and it will find all information about him"
print "Have fun and good luck"

fa=open("Periodictable.csv")
try:
  op=csv.reader(fa)
except:
  print "Error: Verifique el nombre de su archivo"

def lis(x): #Convertir cada elemento a diccionario en una lista
  t=[]
  for em in x:
    tabla={'Simbolo':None,'Numero':None,'Masa atomica':None,'Configuracion':None}
    tabla['Simbolo']=em[1]
    tabla['Numero']=em[0]
    tabla['Masa atomica']=em[3]
    tabla['Configuracion']=em[4]
    #print tabla
    t.append(tabla)
  return t
c=lis(op)

def busqueda(a,b):  #Busqueda
    for i in range (0,len(b)):
        for llave,valor in b[i].items():
            if a==valor:
              for llave,valor in b[i].items():
                print llave,valor

l=False

while l==False: #Repetir el proceso de realizar una busqueda
  j=raw_input("Escriba lo que desea buscar: ")
  busqueda(j,c)
  if (raw_input("Quiere hacer otra busqueda, [si=simon papu]"))=="simon papu":
     pass
  else:
      l=True
#Luis Manuel Garcia Valdivia


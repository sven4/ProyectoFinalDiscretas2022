# Debe instalar las librerias de pysat con los siguientes comandos en cmd:
# pip install python-sat[pblib,aiger]
# pip install python-sat
# pip install -U python-sat
from IPython.utils.sysinfo import num_cpus
from pysat.solvers import Glucose3

# Instanciamos el solver
s = Glucose3()
# Ahora le metemos las clausulas
# El problema es paralelizable y se pudo correr en un tiempo t
# Dos subproblemas no comparten recursos
s.add_clause([1])
# Dos subproblemas distintos no pueden ocupar el mismo nodo:
# -(n resuelve p1) o -(n resuelve p2) o (p1=p2) 
s.add_clause([-2,-3, 4])
# Si un nodo trabaja en un problema, entonces se nodo puede resolver ese problema
# ∀ p, p- ∈ P n_p = n_p- => p = p- 
# n_p != n_p- o p = p-
s.add_clause([-5, 6])
esSatisfacible = s.solve()
valuacionQueSirve = s.get_model()

print("La formula definida es satisfacible? {}".format(esSatisfacible))
if esSatisfacible:
  print("Qué valores de verdad deben tener cada uno de los literales para satisfacerlo? {}".format(valuacionQueSirve))
#R es una lista con los recursos
#S es una lista de subproblemas
#RP es una lista que contiene la lista de las listas derecursos que necesita los subproblemas. Estas estan en un orden tal que si el subproblema i esta en la posición n,
#la lista de recursos de que necesita el subproblema esta en la posicion n de RP
#Ej:
#S[u]= p
#RP[u]= [recursos que  p hece uso]
#N es una lista de los nodos
#NP es una lista que contiene la lista de las listas de nodos capaces de resolver el
#subproblema p. Estas estan en un orden tal que si el subproblema i esta en la posición n,
#la lista de recursos de que necesita el subproblema esta en la posicion n de NP
#Ej:
#S[u]= p
#NP[u]= [nodos capaces de resolver el subproblema p]
#T es una lista que contiene los tiempos, en el orden [tinit [ms],t [ms],tfinal [ms],o tTot [ms]]
Rec=[1,2,3,4,5,6,7,8,9,10]
Sub=[1,2,3]
Recs=[[1,2],[3,4],[5,6]]
No=[1,2,3,4,5,6,7,8,9]
Nop=[[1,2,3,4],[3,4,8,9],[4,5,6,7]]
Tot=[1,2,3,20]

def funcion(R,S,RP,N,NP,T):
  #lista 1 relaciona tiene:(p,w) representa que el subproblema p hace uso del recurso w.
  lista1 = []
  for i in range(len(S)):
    u=S[i]
    for p in range(len(RP[i])):
      ñ=RP[i]
      l=ñ[p]
      lista1.append((u, l))
  print(lista1)
  #lista 2 relaciona tiene:(p,n) representa que el nodo n puede resolver el subproblema p y que el nodo i resuelve subproblema p.

  lista2=[]
  for q in range(len(S)):
    u=S[q]
    for p in range(len(NP[q])):
      ñ=NP[q]
      l=ñ[p]
      lista2.append((u, l))
  print(lista2)
  #Es lista 2 pero en palabras
  listanp=[]
  for i in range(len(lista2)):
    p=lista2[i]
    n=p[0]
    m=p[1]   
    listanp.append("el nodo "+ str(m) + " resuelve subproblema "+ str(n))
  print(listanp)
  # Instanciamos el solver
  s = Glucose3()
  # Ahora le metemos las clausulas
  # El problema es paralelizable y se pudo correr en un tiempo t
  # Dos subproblemas no comparten recursos
  #Tengo que crear función que compare:
  #lista 1 relaciona tiene:(w,p) representa que el subproblema p hace uso del recurso w.
  ####################################################################################################################################
  #Recordar lista1 a restricciones es i: donde va expresion i, mas 1000.
  #Ej lista1[p]=p+1000 
  i=0
  p=0

  # Instanciamos el solver
  s = Glucose3()

  #Instaciamos: Dos subproblemas distintos no pueden ocupar el mismo recurso:
  listaa=[1]
  s.add_clause([1])
  print([1])
  #Recorremos lista 1 y vemos que no haya ningun subproblema que ocupe el mismo recurso que otro subproblema
  #Si hay, agregamos la clausula -1
  for i in range(len(lista1)):
    u=lista1[i]
    ñ=u[1]
    for j in range(len(lista1)):
      k=lista1[j]
      l=k[1]
      if u != k and ñ==l:
        #print(k)
        #print(u)
        s.add_clause([-1])
        listaa.append(-1)
        print([-1])

  # Dos subproblemas distintos no pueden ocupar el mismo nodo:
    for i in range(len(lista2)):
      el1=lista2[i]
      el10=el1[0]
      el11=el1[1]
      for j in range(len(lista1)):
        el2=lista2[j]
        el20=el2[0]
        el21=el2[1]
        if i != j and el21==el11:
          #print(i)
          #print(j)
          li=i+1
          lj=j+1
          s.add_clause([-li,-lj])



  #Todo subproblema se le asigna un nodo y solo un nodo que lo resuelva:
  for i in range(len(lista2)):
      el1=lista2[i]
      el10=el1[0]
      el11=el1[1]
      lis=[]
      li=i+1
      for j in range(len(lista1)):
        el2=lista2[j]
        el20=el2[0]
        el21=el2[1]
        if i != j and el20==el10:
          #print(i)
          #print(j)
          lj=j+1
          lis.append(lj)
      if len(lis)!=0:
        lis.append(li)
        print(lis)
        for k in range(len(lis)):
          lol=lis[k]
          lis2=[]
          lis2.append(-lol)
          for q in range(len(lis)):
            if k!=q:
              lis2.append(lis[q])
          print(lis2)
          s.add_clause(lis2)
  esSatisfacible = s.solve()
  valuacionQueSirve = s.get_model()

  for i in range(len(lista2)):
    el1 = lista2[i]
    

  print("La formula definida es satisfacible? {}".format(esSatisfacible))
  if esSatisfacible:
    print("Qué valores de verdad deben tener cada uno de los literales para satisfacerlo? {}".format(valuacionQueSirve))
    test_list = list("Qué valores de verdad deben tener cada uno de los literales para satisfacerlo? {}".format(valuacionQueSirve))
    ("The original list is : " + str(test_list)) 
    res = [ele for ele in valuacionQueSirve if ele > 0] 
    print("List after filtering : " + str(res)) 
funcion(Rec,Sub,Recs,No,Nop,Tot)

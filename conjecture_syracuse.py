import matplotlib.pyplot as plt

def syracuse(u0):
    lst = []
    lst.append(u0)
    while lst.count(1)!=1:
      if u0>1:
        if u0 % 2 == 0:
            u0 //= 2
        else:
            u0 = 3 * u0 + 1
        lst.append(u0)
    return lst

u0 = int(input("Entrer le premier terme : "))
print(syracuse(u0))
plt.plot(syracuse(u0))
plt.xlabel('n')
plt.ylabel('Valeur')
plt.title('Courbe de la séquence de Syracuse à partir de u0=' + str(u0))
plt.show()
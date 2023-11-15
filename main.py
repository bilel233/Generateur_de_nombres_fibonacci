# Projet generateur de Fibonnacci

# On demande la position du nombre de fibonacci necessaire à l'utilisateur
# puis on le genere
# enfin, on affiche le resultat souhaite

print("========================================")

print("fonction fibonacci")

def fibonacci(n):
    """renvoie le n-ieme terme de la suite de fibonacci"""

    if n == 0:
        return 0        # renvoie le premier terme
    elif n == 1:
        return 1        # renvoie le second terme
    return fibonacci(n-1)+fibonacci(n-2)

# jeux de tests
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(20))
print(fibonacci(25))

print("========================================")

n = int(input("Veuilllez saisir un entier"))        # on saisit un entier

a = fibonacci(n)                    # on stocke le resultat dans la variable a

print("la valeur du n-ieme terme de fibonacci est",a)

####################################################

print("Maintenant, on va generer la position du n-ieme nombre de fibonacci")

def fiboIterative(n):
    """renvoie la position du n'ieme terme de fibonacci ainsi que son n-ieme terme"""
    A=0
    B=1

    cpt = 0             # le pas du compteur
    if n == 0:
        return 0,0
    elif n == 1:
        return 1,1
    for i in range(2,n+1):              # parcourt de 2 à n+1
        C = A + B
        A=B
        B=C

        cpt+=1
    return cpt,C
# jeux de tests
print(fiboIterative(0))
print(fiboIterative(1))
print(fiboIterative(10))

print("========================================")

b = int(input("veuillez saisir un entier"))
res = fiboIterative(b)
print(res)




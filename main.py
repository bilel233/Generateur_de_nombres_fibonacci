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

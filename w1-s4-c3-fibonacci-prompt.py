
def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux petites valeurs de n, on peut retourner n
    if n <= 1:
        return n
    # sinon on initialise f2 pour n-2 et f1 pour n-1
    f2, f1 = 0, 1
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
        print(i, f2, f1)
    # le résultat est dans f1
    return f1
entier = int(input("Entrer un entier "))

print(f"fibonacci({entier}) = {fibonacci(entier)}")

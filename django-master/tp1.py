def somme_entiers(n: int):
    somme = 0.0
    for i in range (n+1):
        somme += i
    return somme
print(somme_entiers(10))
def mystere(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res
print('rest -> ', mystere(10))
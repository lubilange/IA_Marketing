# Fonctions mathématiques de base en Python (sans définition de fonctions)

# 1. Addition de deux nombres
a = 5
b = 3
addition = a + b

# 2. Soustraction de deux nombres
soustraction = a - b

# 3. Multiplication de deux nombres sans l'opérateur '*'
result = 0
for _ in range(abs(b)):
    result += a
multiplication = result if b >= 0 else -result

# 4. Division entière sans l'opérateur '/'
if b == 0:
    raise ValueError("Division par zéro")
quotient = 0
reste = abs(a)
while reste >= abs(b):
    reste -= abs(b)
    quotient += 1
division_entiere = quotient if (a > 0) == (b > 0) else -quotient

# 5. Modulo sans l'opérateur '%'
modulo = a - (division_entiere * b)

# 6. Puissance (exponentiation entière positive)
exp = 3
result = 1
for _ in range(exp):
    result *= a
puissance = result

# 7. Factorielle d'un nombre entier positif
n = 5
result = 1
for i in range(1, n + 1):
    result *= i
factorielle = result

# 8. PGCD (Algorithme d'Euclide)
a, b = 48, 18
while b != 0:
    a, b = b, a - (a // b) * b
pgcd = abs(a)

# 9. PPCM
ppcm = abs(5 * 3) // pgcd

# 10. Vérification si un nombre est premier
n = 29
est_premier = True
if n < 2:
    est_premier = False
for i in range(2, (n // 2) + 1):
    if n - (n // i) * i == 0:
        est_premier = False
        break

# 11. Somme des chiffres d'un nombre
n = 1234
somme = 0
while n > 0:
    somme += n - (n // 10) * 10
    n //= 10
somme_chiffres = somme

# 12. Inversion d'un nombre
n = 1234
inverse = 0
while n > 0:
    inverse = inverse * 10 + (n - (n // 10) * 10)
    n //= 10
inversion_nombre = inverse

# 13. Conversion décimal -> binaire
n = 10
binaire = ""
while n > 0:
    binaire = str(n - (n // 2) * 2) + binaire
    n //= 2
binaire = binaire if binaire else "0"

# 14. Vérification si un nombre est pair
n = 10
est_pair = (n - (n // 2) * 2) == 0

# 15. Vérification si un nombre est impair
est_impair = not est_pair

# D'autres opérations peuvent être ajoutées selon les besoins.
# Fonctions mathématiques avancées en Python (sans définition de fonctions)

# 1. Somme des carrés des n premiers entiers
n = 10
somme_carre = 0
for i in range(1, n + 1):
    somme_carre += i * i

# 2. Produit des n premiers entiers
n = 6
produit = 1
for i in range(1, n + 1):
    produit *= i

# 3. Nombre triangulaire
n = 7
nombre_triangulaire = (n * (n + 1)) // 2

# 4. Vérification si un nombre est parfait
n = 28
somme_diviseurs = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        somme_diviseurs += i
est_parfait = somme_diviseurs == n

# 5. Calcul de la somme des nombres impairs jusqu'à n
n = 10
somme_impairs = 0
for i in range(1, n + 1, 2):
    somme_impairs += i

# 6. Produit des nombres impairs jusqu'à n
n = 7
produit_impairs = 1
for i in range(1, n + 1, 2):
    produit_impairs *= i

# 7. Somme des inverses des entiers jusqu'à n
n = 5
somme_inverse = 0
for i in range(1, n + 1):
    somme_inverse += 1 / i

# 8. Vérification si un nombre est un carré parfait
n = 49
racine_approximative = 0
while racine_approximative * racine_approximative <= n:
    racine_approximative += 1
est_carre_parfait = (racine_approximative - 1) ** 2 == n

# 9. Calcul de la somme des chiffres d'un carré
n = 12
carre = n * n
somme_chiffres_carre = 0
while carre:
    somme_chiffres_carre += carre % 10
    carre //= 10

# 10. Vérification si un nombre est un multiple d'un autre
a, b = 24, 6
est_multiple = (a % b) == 0

# 11. Calcul de la différence entre le carré de la somme et la somme des carrés des n premiers entiers
n = 10
somme = (n * (n + 1)) // 2
somme_carre = 0
for i in range(1, n + 1):
    somme_carre += i * i
difference_sommes = somme ** 2 - somme_carre

# 12. Vérification si un nombre est palindrome numériquement
n = 12321
original, inverse = n, 0
while original:
    inverse = inverse * 10 + (original % 10)
    original //= 10
est_palindrome = n == inverse

# 13. Conversion d'un entier en base 3
n = 19
base3 = ""
while n:
    base3 = str(n % 3) + base3
    n //= 3
base3 = base3 if base3 else "0"

# 14. Calcul du produit des chiffres d'un nombre
n = 432
produit_chiffres = 1
while n:
    produit_chiffres *= n % 10
    n //= 10

# 15. Détermination du chiffre le plus grand d'un nombre
n = 4897
max_chiffre = 0
while n:
    max_chiffre = max(max_chiffre, n % 10)
    n //= 10

# 16. Détermination du chiffre le plus petit d'un nombre
n = 4897
min_chiffre = 9
while n:
    min_chiffre = min(min_chiffre, n % 10)
    n //= 10

# 17. Vérification si un nombre est un nombre de Mersenne
n = 31
est_mersenne = ((n + 1) & n) == 0

# 18. Conversion d'un nombre décimal en hexadécimal
n = 254
hexadecimal = ""
chiffres = "0123456789ABCDEF"
while n:
    hexadecimal = chiffres[n % 16] + hexadecimal
    n //= 16
hexadecimal = hexadecimal if hexadecimal else "0"

# 19. Vérification si un nombre est un carré parfait en testant les derniers chiffres
n = 64
dernier_chiffre = n % 10
est_carre_parfait = dernier_chiffre in [0, 1, 4, 5, 6, 9]

# 20. Vérification si un nombre est une puissance de 2
n = 16
est_puissance_de_2 = (n & (n - 1)) == 0 and n != 0

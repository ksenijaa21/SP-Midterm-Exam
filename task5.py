n = int(input("Unesite broj redova kvadratne matrice: "))
X = []

for i in range(n):

    X.append([])

    for j in range(n):
        jedan_elemenat = int(input("Unesi element: "))
        X[i].append(jedan_elemenat)

zbir_glavne_dijagonale = sum(X[i][i] for i in range(n))
zbir_sporedne_dijagonale = sum(X[n-i-1][n-i-1] for i in range(n))

for vektor in X:
    print(vektor)

print("Zbir glavne dijagonale je: " + str(zbir_glavne_dijagonale))
print("Zbir sporedne dijagonale je: " + str(zbir_sporedne_dijagonale))


suma = 0

specijalni_brojevi = 0

print("Unesite broj ili '=' ")

while True:
    x = input()

    if x == '=':
        print("Srednja vrijednost je: " + str(srednja_vrijednost))
        break


    if int(x) % 3 == 0 and not int(x) % 5 == 0:
        suma += int(x)
        specijalni_brojevi +=1

        srednja_vrijednost = (int(suma)) / (int(specijalni_brojevi))
def recStep(p, d):
    print(str(p))

    while True:
        if d < 0:
            if n > 0:
                recStep(p-m, d)
            else:
                recStep(p+m, d * -1)
        else:
            if p < n:
                recStep(p+m, d)
            else:
                return


n = int(input("N: "))
m = int(input("M: "))

recStep(n, -1)
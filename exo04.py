def __init__():
    try:
        n = int(input("n= "))
    except ValueError:
        print("Un entier merde.")
        exit()
    print(treat(n))

def treat(n):
    t = 0
    for i in range(n):
        if (i<=10):
            prixDeBase = 0.2
        if (i>10 and i<=20):
            prixDeBase = 0.18
        if (i>20):
            prixDeBase = 0.15
        t = t + prixDeBase
    return "{} photocopies font {} euros.".format(n, t)

if __name__ == '__main__':
    __init__()

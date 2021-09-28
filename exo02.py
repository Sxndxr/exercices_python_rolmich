def __init__():
        a = float(input("Premier nombre: "))
        b = float(input("Second Nombre: "))
        print(moy(a,b))
def moy(a,b):
    c = (a+b)/2
    return "La moyenne de {} et {} est {}.".format(a,b,c)

if __name__ == '__main__':
    __init__()
def __init__():
        l = []
        a = float(input("Premier Nombre: "))
        l.append(a)
        b = float(input("Second Nombre: "))
        l.append(b)
        c = float(input("Troisième Nombre: "))
        l.append(c)
        print(milieu(l))
    
def milieu(l):
    s = sorted(l)
    return "Le nombre entre {}, {} et {} est {}".format(l[0],l[1],l[2],s[1])

if __name__ == '__main__':
    __init__()
def imprimir_fig(letra):
    print("\n"+letra*4)
    print(letra)
    print(letra)
    print(letra)
    print(letra*4+"\n")

    print("\n"+letra*4)
    print(letra+"  "+letra)
    print(letra+"  "+letra)
    print(letra+"  "+letra)
    print(letra*4+"\n")

    print("\n"+letra*3)
    print(letra+"  "+letra)
    print(letra+"  "+letra)
    print(letra+"  "+letra)
    print(letra*3+"\n")

    print("\n"+letra*4)
    print(letra)
    print(letra*3)
    print(letra)
    print(letra*4+"\n")


letra = input("Con que letras quiere armar la figura? ")

imprimir_fig(letra)

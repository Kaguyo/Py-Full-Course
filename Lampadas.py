def main():
    n = int(input("Clicks no interruptor: "))
    a = 0
    b = 0

    lista = []

    for _ in range(n):
        elemento = input("Digite um elemento: ")
        lista.append(elemento)

    for posicoes in lista:
        if posicoes == 1:
            a += 1
        else: a += 1; b += 1
    
    if a % 2 > 0 : print(1)
    else: print(0)
    if b % 2 > 0 : print(1)
    else: print(0)

if __name__ == "__main__":
    main()
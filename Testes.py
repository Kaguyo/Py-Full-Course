
def main():
    n = int(input("Digite um valor inteiro: "))
    i = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        i = i + 1
    
    print("A quantidade de vezes que a função foi chamada foi:",i)

main()

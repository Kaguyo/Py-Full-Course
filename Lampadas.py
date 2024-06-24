# 1a Versão
def main():
    try: # tente executar o que há dentro do bloco de código, se der erro.:except
        n = int(input("Clicks no interruptor: "))

    # Get clicks and switch presses in a single line
        clicks_and_presses = input("Aperte interruptor 1 ou 2: ").split() # Split é interpretado como "spacebar".

        # Ensure enough input provided
        if len(clicks_and_presses) < n:
            print("Error: Not enough switch presses provided.")
            return

        lamp_a = False  # Initially off
        lamp_b = False  # Initially off

        # Process switch presses
        for press in clicks_and_presses:
            switch_press = int(press)

            if switch_press == 1:
                lamp_a = not lamp_a  # Toggle lamp A
            elif switch_press == 2:
                lamp_a = not lamp_a
                lamp_b = not lamp_b  # Toggle both lamps

        # Print final lamp states
        print(1 if lamp_a else 0)  # Lamp A state
        print(1 if lamp_b else 0)  # Lamp B state

    except ValueError: # Por padrão qualquer erro desse tipo, vai cair nessa estrutura.
       print("Valor precisa ser um número")
    except Exception: # Por padrão qualquer erro vai cai nessa estrutura.
        print("Perdemo")
       

if __name__ == "__main__":
    main()

# -/-

# 2a Versão
def main():

    n = int(input("Número de cliques no interruptor: "))
    a = 0
    b = 0

    interruptor = []
    while len(interruptor) < n:
        interruptor += input("Digite apenas um elemento, sendo 1 ou 2: ")
        if interruptor == n:
            break 
    print(interruptor)

    for posicoes in (interruptor):
        if posicoes == str(1):
            a += 1
        elif posicoes == str(2): 
            a += 1; b += 1
        else:
            print("Valor invalido de interruptor. (1 ou 2)")
            return
    
    if a % 2 > 0 : print(1)
    else: print(0)
    if b % 2 > 0 : print(1)
    else: print(0)

if __name__ == "__main__":
    main()

# -/-

# 3a Versão
def main():
    n = int(input("Clicks no interruptor: "))
    a = 0
    b = 0

    lista = []

    for _ in range(n):
        elemento = input("Digite um elemento: ")
        lista.append(elemento)

    for posicoes in lista:
        if posicoes == str(1):
            a += 1
        elif posicoes == str(2): 
            a += 1; b += 1
        else:
            print("Erro de valores.")
    
    if a % 2 > 0 : print(1)
    else: print(0)
    if b % 2 > 0 : print(1)
    else: print(0)

if __name__ == "__main__":
    main()
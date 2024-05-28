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

def main():
    n = int(input("Clicks no interruptor: "))
    a = 0
    b = 0

    interruptor = input("Aperte interruptor 1 ou 2: ").split(" ")
    
    for posicoes in (interruptor):
        print(posicoes)
        if posicoes == 1:
            a += 1
        else: a += 1; b += 1
    
    if a % 2 > 0 : print(1)
    else: print(0)
    if b % 2 > 0 : print(1)
    else: print(0)

if __name__ == "__main__":
    main()

# -/-

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
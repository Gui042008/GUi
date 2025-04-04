palavra = "escola"
limite_tentativa = len(palavra) + 5

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("__")



contador = 1
while(contador <= limite_tentativa):
    print(letras_acertadas)
    print("Tentativas",contador,"/",limite_tentativa)
    chute = input("Digite a letra:")

    indice = 0
    for letra in palavra:
        if chute ==letra:
            letras_acertadas[indice] =chute
        indice = indice +1    
     
            




    contador = contador +1

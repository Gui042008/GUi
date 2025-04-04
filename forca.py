palavra = "escola"
limite_tentativa = len(palavra) + 5
letras_adivinhadas = []
acertos = ["_"] * len(palavra)

contador = 1
while contador <= limite_tentativa:
    print("Tentativas", contador, "/", limite_tentativa)
    print("Palavra:", " ".join(acertos))
    chute = input("Digite a letra: ").lower()

    if chute in letras_adivinhadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(chute)

    if chute in palavra:
        print("Você acertou uma letra!")
        for index, letra in enumerate(palavra):
            if letra == chute:
                acertos[index] = chute
    else:
        print("Letra não está na palavra.")

    if "_" not in acertos:
        print("Parabéns! Você adivinhou a palavra:", palavra)
        break

    contador += 1

if "_" in acertos:
    print("Você não conseguiu adivinhar a palavra. A palavra era:", palavra)
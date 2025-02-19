import random
sorteio = random.randint (1,10)
print ("####### Jogo da Adivinhacao ######")
print ("Adivinhe o numero que estou pensando")
chute = int( input (" Digite seu chute "))
#print (sorteio)
#print(chute)
print (sorteio)
print (chute)
if (chute == sorteio):
    print("Parabens , voce  acertou numero era",sorteio)
if (chute! = sorteio):
    print ("voce errou",sorteio)
        
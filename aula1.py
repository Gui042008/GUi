import random
sorteio = random.randint (1,10)
print ("####### Jogo da Adivinhacao ######")
print ("Adivinhe o numero que estou pensando")
chute = int( input (" Digite seu chute "))
limite_tentativas = 3
tentativas = 1
while (limite_tentativas >= tentativas)
chute = int( input (" Digite seu chute "))

print ("tentativas:", tentativas)
#tentativas = tentativas + 1
#print (sorteio)
#print(chute)
print (sorteio)
print (chute)
if (chute == sorteio):
    print("Parabens , voce  acertou numero era",sorteio)



        
import random
sorteio = random.randint (1,10)
print ("####### Jogo da Adivinhacao ######")
print ("Adivinhe o numero que estou pensando4")
       
limite_tentativas = 3
tentativas = 1
while (limite_tentativas >= tentativas):

    print ("tentativas:", tentativas)
    chute = int( input (" Digite seu chute "))
    if (chute == sorteio):
        print("Parabens , voce  acertou numero era",sorteio)
    elif (chute > sorteio):
        print ("chute um numero menor")
    elif(chute < sorteio):
        print ("Chute  um numero maior")
        

    





        
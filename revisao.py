nome = "Guilherme Rodrigues V"  
numero_chamada = 11 


print("Bem-vindo(a), A minha revisao! Este código foi desenvolvido por",nome,", numero da chama:",numero_chamada)




altura = 1.80  
musica_favorita = "Vidigal"  
filme_favorito = "One piece"  
nota_filme_favorito = 9.0 


altura_usuario = float(input("Por favor, digite sua altura em metros: "))
if altura_usuario > altura:
    print("Você é maior que eu.")
else:
    print("Você é menor ou igual a mim.")


musicas_usuario = []
for i in range(3):
    musica = input("Digite uma música que você gosta: ")
    musicas_usuario.append(musica)


if musica_favorita in musicas_usuario:
    print(f"Você gosta da minha música favorita: {musica_favorita}!")
else:
    print(f"Você não gosta da minha música favorita: {musica_favorita}.")


filmes = []
notas = []
for i in range(3):
    filme = input("Digite o nome de um serie que você gosta: ")
    nota = float(input(f"Qual a nota do serie {filme} no IMDb? "))
    filmes.append(filme)
    notas.append(nota)


for i in range(len(filmes)):
    if notas[i] > nota_filme_favorito:
        print(f"A Seria {filmes[i]} tem uma nota maior que o meu sere favorito.")
    elif notas[i] < nota_filme_favorito:
        print(f"A Serie {filmes[i]} tem uma nota menor que o meu sere favorito.")
    else:
        print(f"A Serie {filmes[i]} tem a mesma nota que o meu sere favorito.")
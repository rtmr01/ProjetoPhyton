import os 
os.system ('clear')

livros = []
while True:
    resposta = input("Você quer continuar a cadastrar livros? (Sim/Não): ")
    if resposta.lower() == "não":
        break

    cadastro = {
        "Nome": input("Digite o nome do livro: "),
        "Autor": input("Digite o autor do livro: "),
        "Categoria": str(input("Digite a categoria do livro: ")),
        "Preço": float(input("Digite o preço do livro: "))
    }
    livros.append(cadastro)

print(livros)



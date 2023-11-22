import os 
os. system ('clear')
total = 0
livros = []

def carregar_livros():
    global total, livros
    try:
        with open('biblioteca.txt', 'r') as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                partes = linha.strip().split(': ')
                livro = {"Nome": partes[1], "Autor": partes[3], "Categoria": partes[5], "Preço": float(partes[7])}
                livros.append(livro)
                total += livro["Preço"]
    except FileNotFoundError:
        pass

def salvar_livros():
    with open('biblioteca.txt', 'w') as arquivo:
        for livro in livros:
            arquivo.write(f'Nome: {livro["Nome"]}\nAutor: {livro["Autor"]}\nCategoria: {livro["Categoria"]}\nPreço: {livro["Preço"]}\n\n')

def adicionar_livro():
    global total
    carregar_livros()
    cadastro = {
        "Nome": input("Digite o nome do livro: "),
        "Autor": input("Digite o autor do livro: "),
        "Categoria": input("Digite a categoria do livro: "),
        "Preço": float(input("Digite o preço do livro: "))  
    }
    total += cadastro["Preço"]
    livros.append(cadastro)
    salvar_livros()
    print("Livro cadastrado com sucesso.")

def visualizar_livros():
    global livros
    carregar_livros()
    if not livros:
        print("Nenhum livro cadastrado ainda.")
    else:
        for livro in livros:
            print("\nLivro:")
            for chave, valor in livro.items():
                print(f"{chave}: {valor}")

def excluir_livro():
    global total, livros
    carregar_livros()
    visualizar_livros()
    if livros:
        nome_livro = input("Digite o nome do livro que você quer excluir: ")
        livro_encontrado = None

        for livro in livros:
            if livro["Nome"].lower() == nome_livro.lower():
                livro_encontrado = livro
                break

        if livro_encontrado:
            total = total - livro_encontrado["Preço"]  # Subtrai o preço do livro removido
            livros.remove(livro_encontrado)
            salvar_livros()
            print(f"O livro {livro_encontrado['Nome']} foi removido.")
        else:
            print("Livro não encontrado.")
    else:
        print("Não há livros para excluir.")

def mostrar_soma_precos():
    global total
    carregar_livros()
    print(f'Total acumulado: {total:.2f}')

while True:
    opcao = input("\nEscolha uma opção:\n1 Adicionar livro\n2 Visualizar livros\n3 Excluir livro\n4 Sair\n5 Ver Total\nOpção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        visualizar_livros()
    elif opcao == "3":
        excluir_livro()
    elif opcao == "4":
        break
    elif opcao == "5":
        mostrar_soma_precos()
    else:
        print("Opção inválida. Tente novamente.")
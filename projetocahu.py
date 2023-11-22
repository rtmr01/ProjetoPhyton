import os
os.system('cls')

biblioteca = []


def adicionar_livro():
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    categoria = input("Digite a categoria do livro: ")
    preco = float(input("Digite o preço do livro: "))
    livro = {
        "nome": nome,
        "autor": autor,
        "categoria": categoria,
        "preco": preco
    }
    biblioteca.append(livro)
    print("Livro adicionado com sucesso!")

def visualizar_livros():
    if not biblioteca:
        print("Nenhum livro na biblioteca.")
    else:
        for index, livro in enumerate(biblioteca, start=1):
            print(f"{index}. Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Preço: R${livro['preco']:.2f}")

def atualizar_livro():
    visualizar_livros()
    indice = int(input("Digite o índice do livro a ser atualizado: "))
    if 1 <= indice <= len(biblioteca):
        nome = input("Digite o novo nome do livro: ")
        autor = input("Digite o novo nome do autor: ")
        categoria = input("Digite a nova categoria do livro: ")
        preco = float(input("Digite o novo preço do livro: "))
        livro = {
            "nome": nome,
            "autor": autor,
            "categoria": categoria,
            "preco": preco
        }
        biblioteca[indice - 1] = livro
        print("Livro atualizado com sucesso!")
    else:
        print("Índice inválido.")

def excluir_livro():
    visualizar_livros()
    indice = int(input("Digite o índice do livro a ser excluído: "))
    if 1 <= indice <= len(biblioteca):
        del biblioteca[indice - 1]
        print("Livro excluído com sucesso!")
    else:
        print("Índice inválido.")

def visualizar_por_categoria():
    categoria = input("Digite a categoria para visualizar os livros: ")
    livros_por_categoria = [livro for livro in biblioteca if livro['categoria'].lower() == categoria.lower()]
    if livros_por_categoria:
        print(f"Livros na categoria '{categoria}':")
        for livro in livros_por_categoria:
            print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Preço: R${livro['preco']:.2f}")
    else:
        print(f"Nenhum livro encontrado na categoria '{categoria}'.")

def calcular_gastos_totais():
    total = sum(livro['preco'] for livro in biblioteca)
    print(f"Total gasto em livros: R${total:.2f}")

def extrato_por_categoria():
    categorias = []
    for livro in biblioteca:
        categoria = livro['categoria']
        if categoria not in categorias:
            categorias.append(categoria)

    print("Extrato da Biblioteca por Categoria:")
    for categoria in categorias:
        print(f"\nCategoria: {categoria}")
        livros_por_categoria = [livro for livro in biblioteca if livro['categoria'] == categoria]
        if livros_por_categoria:
            for livro in livros_por_categoria:
                print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Preço: R${livro['preco']:.2f}")
        else:
            print("Nenhum livro encontrado nesta categoria.")


#essa def serve para iniciar a biblioteca como uma lista. se essa funcao nao exisitisse, a biblioteca enquanto lista nao abriria nada, por mais que tenha muita coisa na biblioteca.txt



biblioteca=[]
while True:
    print("\n=== Menu ===")
    print("1. Adicionar livro")
    print("2. Visualizar todos os livros")
    print("3. Atualizar livro")
    print("4. Excluir livro")
    print("5. Visualizar por categoria")
    print("6. Acompanhamento de Gastos Totais")
    print("7. Extrato da Biblioteca por Categoria")
    print("8. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_livro()
    elif escolha == "2":
        visualizar_livros()
    elif escolha == "3":
        atualizar_livro()
    elif escolha == "4":
        excluir_livro()
    elif escolha == "5":
        visualizar_por_categoria()
    elif escolha == "6":
        calcular_gastos_totais()
    elif escolha == "7":
        extrato_por_categoria()
    elif escolha == "8":
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Tente novamente.")

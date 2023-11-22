import os
os.system('clear')

biblioteca = []
total=0

def adicionar_livro():
    global total
    with open ('biblioteca.txt', 'a') as arquivo:
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
        total += livro["preco"]
        biblioteca.append(livro)
        print("Livro adicionado com sucesso!")
        linha = f"Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Preço: {livro['preco']}\n"
        arquivo.write(linha)
        arquivo.write(f'Total gasto: {total}\n')

def visualizar_livros():
    with open ('biblioteca.txt','r') as biblioteca:
        conteudo= biblioteca.read()
        print(f'Conteudo da sua biblioteca', conteudo)


def atualizar_livro():
    visualizar_livros()
    nome_antigo = input("Digite o nome do livro a ser atualizado: ")
    for i in range(len(biblioteca)):
        if biblioteca[i]["nome"] == nome_antigo:
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
            biblioteca[i] = livro
            with open('biblioteca.txt', 'w') as f:
                for livro in biblioteca:
                    f.write(f'{livro["nome"]},{livro["autor"]},{livro["categoria"]},{livro["preco"]}\n')
            print("Livro atualizado com sucesso!")
            return
    print("Livro não encontrado.")


def excluir_livro_por_nome():
    global total
    visualizar_livros()
    nome_livro = input("Digite o nome do livro a ser excluído: ")
    livros_para_excluir = [livro for livro in biblioteca if livro['nome'].lower() == nome_livro.lower()]

    if livros_para_excluir:
        for livro in livros_para_excluir:
            total -= livro["preco"]
            biblioteca.remove(livro)
            print(f"Livro '{livro['nome']}' excluído com sucesso!")

        with open('biblioteca.txt', 'w') as f:
            for livro in biblioteca:
                f.write(f'{livro["nome"]},{livro["autor"]},{livro["categoria"]},{livro["preco"]}\n')
                
    else:
        print(f"Livro '{nome_livro}' não encontrado.")


#nao funciona
def buscar_por_categoria():
    categoria_procurada = input("Digite a categoria a ser buscada: ")
    livros_encontrados = []

    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        nome, autor, categoria, preco = linha.strip().split(',')
        if categoria.lower() == categoria_procurada.lower():
            livros_encontrados.append(nome)

    if livros_encontrados:
        print(f"Livros na categoria '{categoria_procurada}':")
        for nome_livro in livros_encontrados:
            print(f"- {nome_livro}")
    else:
        print("Categoria não encontrada.")






def calcular_gastos_totais():
    print (total)



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
        excluir_livro_por_nome()
    elif escolha == "5":
        buscar_por_categoria()
    elif escolha == "6":
        calcular_gastos_totais()
    elif escolha == "7":
        extrato_por_categoria()
    elif escolha == "8":
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Tente novamente.")

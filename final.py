import os 
os.system ('clear')

biblioteca = []
total = 0

def adicionar_livro():
    global total
    with open('biblioteca.txt', 'a') as arquivo:
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        categoria = input("Digite a categoria do livro: ")
        preco = float(input("Digite o preço do livro: "))
        paginas = int(input("Digite a quantidade de páginas do livro: "))
        livro = {
            "nome": nome,
            "autor": autor,
            "categoria": categoria,
            "preco": preco,
            "paginas": paginas
        }
        total += livro["preco"]
        biblioteca.append(livro)
        print("Livro adicionado com sucesso!")
        linha = f"Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Preço: {livro['preco']}, Páginas: {livro['paginas']}, Total: {total}\n"
        arquivo.write(linha)

def visualizar_livros():
    with open('biblioteca.txt', 'r') as biblioteca:
        conteudo = biblioteca.read()
        print(f'Conteúdo da sua biblioteca:\n{conteudo}\n')


def atualizar_livro():
    if not biblioteca:
        print("Nenhum livro na biblioteca.")
        return

    visualizar_livros()
    nome_antigo = input("Digite o nome do livro a ser atualizado: ")

    for i in range(len(biblioteca)):
        if biblioteca[i]["nome"] == nome_antigo:
            nome = input("Digite o novo nome do livro: ")
            autor = input("Digite o novo nome do autor: ")
            categoria = input("Digite a nova categoria do livro: ")
            preco = float(input("Digite o novo preço do livro: "))

            total -= biblioteca[i]["preco"]
            total += preco

            livro = {
                "nome": nome,
                "autor": autor,
                "categoria": categoria,
                "preco": preco
            }
            biblioteca[i] = livro

            with open('biblioteca.txt', 'w') as f:
                for livro in biblioteca:
                    linha = f"Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Preço: {livro['preco']}, Páginas: {livro['paginas']}, Total: {total}\n"
                    f.write(linha)

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
                linha = f"Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Preço: {livro['preco']}, Páginas: {livro['paginas']}, Total: {total}\n"
                f.write(linha)

    else:
        print(f"Livro '{nome_livro}' não encontrado.")



def buscar_por_categoria():
    categoria_procurada = input("Digite a categoria a ser buscada: ")
    livros_encontrados = []

    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        campos = linha.strip().split(', ')
        livro_info = {}
        for campo in campos:
            chave, valor = campo.split(': ')
            livro_info[chave] = valor

        if 'Categoria' in livro_info and livro_info['Categoria'].lower() == categoria_procurada.lower():
            nome = livro_info.get('Nome', '')
            autor = livro_info.get('Autor', '')
            preco = livro_info.get('Preço', '')

            livro = f"Nome: {nome}, Autor: {autor}, Preço: {preco}"
            livros_encontrados.append(livro)

    if livros_encontrados:
        print(f"Livros na categoria '{categoria_procurada}':")
        for livro_info in livros_encontrados:
            print(f"- {livro_info}")
    else:
        print("Categoria não encontrada.")



def calcular_gasto_final():
    gastofinal = 0

    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        campos = linha.strip().split(', ')
        livro_info = {}
        for campo in campos:
            chave, *valor = campo.split(': ')
            valor = ': '.join(valor)
            livro_info[chave] = valor

        if 'Preço' in livro_info:
            preco = float(livro_info['Preço'])
            gastofinal += preco

    print(f"Gasto final com livros: R${gastofinal}")
    return gastofinal



def extrato_por_categoria():
    categorias = {}

    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        campos = linha.strip().split(', ')
        livro_info = {}
        for campo in campos:
            chave, valor = campo.split(': ')
            livro_info[chave] = valor

        if 'Categoria' in livro_info:
            categoria = livro_info['Categoria']
            nome = livro_info.get('Nome', '')

            if categoria not in categorias:
                categorias[categoria] = [nome]
            else:
                categorias[categoria].append(nome)

    print("Extrato da Biblioteca por Categoria:")
    for categoria, livros in categorias.items():
        print(f"\nCategoria: {categoria}")
        for livro in livros:
            print(f"- {livro}")



def buscar_por_paginas():
    paginas_procuradas = int(input("Digite a quantidade de páginas desejada: "))
    livros_encontrados = []

    with open('biblioteca.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        for linha in linhas:
            campos = linha.strip().split(', ')
            livro_info = {}
            for campo in campos:
                chave, valor = campo.split(': ')
                livro_info[chave] = valor

            if 'Páginas' in livro_info and int(livro_info['Páginas']) <= paginas_procuradas:
                livro = f"Nome: {livro_info.get('Nome', '')}, Autor: {livro_info.get('Autor', '')}, Categoria: {livro_info.get('Categoria', '')}, Preço: {livro_info.get('Preço', '')}, Páginas: {livro_info.get('Páginas', '')}"
                livros_encontrados.append(livro)

    if livros_encontrados:
        print(f"Livros com {paginas_procuradas} páginas ou menos:")
        for livro_info in livros_encontrados:
            print(f"- {livro_info}")
    else:
        print(f"Nenhum livro encontrado com {paginas_procuradas} páginas ou menos.")

while True:
    print("\n=== Menu ===")
    print("1. Adicionar livro")
    print("2. Visualizar todos os livros")
    print("3. Atualizar livro")
    print("4. Excluir livro")
    print("5. Visualizar por categoria")
    print("6. Acompanhamento de Gastos Totais")
    print("7. Extrato da Biblioteca por Categoria")
    print("8. Buscar por quantidade de páginas")
    print("9. Sair")

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
        calcular_gasto_final()
    elif escolha == "7":
        extrato_por_categoria()
    elif escolha == "8":
        buscar_por_paginas()
    elif escolha == "9":
        print("Saindo do programa...")
        break
    else:
        print("Escolha inválida. Tente novamente.")



import os 
os.system ('clear')
total = 0
livros = []


def adicionar_livro():
    global total
    
    with open('biblioteca.txt', 'a') as arquivo:
        cadastro = {
            "Nome": input("Digite o nome do livro: "),
            "Autor": input("Digite o autor do livro: "),
            "Categoria": input("Digite a categoria do livro: "),
            "Preço": float(input("Digite o preço do livro: "))
        }

        total += cadastro["Preço"]
        livros.append(cadastro)

        
        linha = f"Nome: {cadastro['Nome']}, Autor: {cadastro['Autor']}, Categoria: {cadastro['Categoria']}, Preço: {cadastro['Preço']}\n"
        arquivo.write(linha)
        
        
        arquivo.write(f'Total gasto: {total}\n')

    print("Livro cadastrado com sucesso.")

def visualizar_livros():
    with open ('biblioteca.txt','r') as biblioteca:
        conteudo= biblioteca.read()
        print(f'COnteudo da sua biblioteca', conteudo)

def excluir_livro():
    global total

    nome_livro = input("Digite o nome do livro que deseja excluir: ")

    with open('arquivo.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    livro_removido = None  

    with open('arquivo.txt', 'w') as arquivo:
        for linha in linhas:
            if nome_livro not in linha:
                arquivo.write(linha)
            else:
                
                livro_removido = [livro for livro in livros if livro["Nome"] == nome_livro]
                if livro_removido:
                    total -= livro_removido[0]["Preço"]
                    livros.remove(livro_removido[0])

    if livro_removido:
        print(f"Livro '{nome_livro}' excluído com sucesso.")
        print(f"Total gasto atualizado: {total}")
    else:
        print(f"Livro '{nome_livro}' não encontrado.")

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
    else:
        print("Opção inválida. Tente novamente.")

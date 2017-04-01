produtos = {}

def cadastrarProduto(produtos,produto,preco):
    produtos[produto] = preco
    print(produtos)
    return produtos

def exibirProdutos(produtos):
    print("Produtos cadastrados:")
    print(produtos,"\n")

def removerProduto(remover):
    produtos.pop(remover)
    print("Produto removido!")

def exibirCaroProduto(produtos):
    Caro = max(produtos.keys())
    print("O produto mais caro é:",Caro)

def exibirBaratoProduto(produtos):
    Barato = min(produtos.keys())
    print("O produto mais barato é:",Barato)

def menu():
    x = 0
    while(x == 0):
        Informe = int(input("Digite 1 para cadastrar um produto.\n Digite 2 para exibir os produtos.\n Digite 3 para remover um produto.\n Digite 4 para exibir o produto mais caro.\n Digite 5 para exibir o produto mais barato.\n Digite 6 para sair.\n"))
        if(Informe == 1):
            produto = str(input("Digite o nome do produto:"))
            preco = float(input("Digite o preço deste produto:"))
            cadastrarProduto(produtos,produto,preco)
        elif(Informe == 2):
            exibirProdutos(produtos)
        elif(Informe == 3):
            remover = str(input("Digite o nome do produto no qual você quer remover:"))
            removerProduto(remover)
        elif(Informe == 4):
            exibirCaroProduto(produtos)
        elif(Informe == 5):
            exibirBaratoProduto(produtos)
        elif(Informe == 6):
            x = 1
            print("Obrigado!")
        else:
            print("Opção não válida!")
menu()

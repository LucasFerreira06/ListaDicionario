funcionarios = {}

def adicionarFuncionario(matricula,nome):
    if matricula in funcionarios:
        print("Matrícula já existente!")
    else:
        funcionarios[matricula] = nome
        print(funcionarios)
        
    return funcionarios

def buscarFuncionarios(matricula):
    if matricula in funcionarios:
        print("Funcionário:",funcionarios[matricula])
    else:
        print("Matrícula não cadastrada!")

def exibirFuncionario(funcionarios):
    for a in funcionarios:
        print("Funcionário (Matrícula):",a)

def menu():
    x = 0
    while(x == 0):
        OpcaoMenu = int(input("Digite 1 para adicionar um funcionário; Digite 2 para buscar um funcionário; Digite 3 para exibir os funcionários; Digite 4 para sair."))
        if(OpcaoMenu == 1):
            matricula = int(input("Digite a matrícula do funcionário:"))
            nome = str(input("Digite o nome do funcionário:"))
            adicionarFuncionario(matricula,nome)
        elif(OpcaoMenu == 2):
            matricula = int(input("Digite a matrícula do funcionário:"))
            buscarFuncionarios(matricula)
        elif(OpcaoMenu == 3):
            exibirFuncionario(funcionarios)
        elif(OpcaoMenu == 4):
            x = 1
            print("Obrigado!")
        else:
            print("Opção não válida!")

menu()

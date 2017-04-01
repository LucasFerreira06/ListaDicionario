dias = []

def adicionarDia(posicao,dia):
    diasSemana = {}
    diasSemana[posicao] = dia
    dias.append(diasSemana)
    menu()

def exibirDias(dias):
    for dia in dias:
        for posicao,nomeDia in dia.items():
            print(posicao,"-",nomeDia)
    menu()

def menu():
    Informe = int(input("Digite 1 para adicionar o dia e o nome da semana. Digite 2 para exibir os dias e 3 para sair.:"))
    if (Informe == 1):
        posicao = int(input("Digite a posição do dia:"))
        dia = str(input("Digite o nome do dia:"))
        adicionarDia(posicao,dia)

    elif (Informe == 2):
        exibirDias(dias)

    elif (Informe == 3):
        print("Obrigado!")

    else:
        print("Opção inválida!")

menu()

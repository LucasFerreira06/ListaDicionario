turmas = {}

def adicionarTurma():
    NomeT = str(input("Adicione o nome de sua turma:"))
    Alunos = {}
    turmas[NomeT] = Alunos
    print("Turmas:",turmas)

def adicionarAlunoNotas():
    TurmaNome = str(input("Digite o nome da turma do aluno:"))
    if(TurmaNome in turmas):
        print("Turma:",turmas[TurmaNome])
        Alunos = {}
        Matricula = int(input("Digite a matricula do aluno:"))
        Notas = []
        add = "Sim"
        while(add == "Sim"):
            Nota = float(input("Digite a nota do aluno:"))
            Notas.append(Nota)
            add = str(input("Se tiver mais de uma nota, digite: Sim, se não, digite: Não:"))
        turmas[TurmaNome][Matricula] = Notas
        print("Turma:",turmas[TurmaNome])
    else:
        print("Turma não existente!")

def calcularMedia(Notas):
    Soma = 0
    for a in Notas:
        Soma = Soma + a
        Media = Soma/len(Notas)
    return(Media)

def mediaDaTurma():
    Soma = 0
    Contador = 0
    TurmaNome = str(input("Digite o nome da turma:"))
    if(TurmaNome in turmas):
        for i in turmas[TurmaNome]:
            Soma = Soma + calcularMedia(turmas[TurmaNome][i])
            Contador = Contador + 1
        Media = Soma/Contador
        print("Média da Turma:",Media)
    else:
        print("Turma não existente!")
    return

def main():
    Contador = 1
    while(Contador > 0):
        print("Digite 1 para adicionar a turma.")
        print("Digite 2 para adicionar o aluno e as notas.")
        print("Digite 3 para calcular a média de um aluno.")
        print("Digite 4 para calcular a média de uma Turma.")
        OpcaoMenu = int(input(""))
        if(OpcaoMenu == 1):
            adicionarTurma()
        elif(OpcaoMenu == 2):
            adicionarAlunoNotas()
        elif(OpcaoMenu == 3):
            Turma = str(input("Digite a turma:"))
            if(Turma in turmas):
                Matricula = int(input("Digite a matricula do aluno:"))
                if(Matricula in turmas[Turma]):
                    print("Média do aluno:",calcularMedia(turmas[Turma][Matricula]))
                else:
                    print("Matrícula não existente!")
            else:
                print("Turma não existente!")
        elif(OpcaoMenu == 4):
            mediaDaTurma()
        else:
            print("Opção não válida!")
if __name__ == "__main__":
    main()

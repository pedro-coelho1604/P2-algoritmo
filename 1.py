def cadastrar_nome(agenda):
    while True:
        nome = input("Digite o nome (ou digite 0 para voltar): ")
        if nome == '0':
            return
        endereco = input("Digite o endereço: ")
        telefone = input("Digite o telefone: ")
        agenda.append({'Nome': nome, 'Endereço': endereco, 'Telefone': telefone})
        print("Nome cadastrado com sucesso!")

def consultar_nome(agenda):
    while True:
        nome = input("Digite o nome a ser consultado (ou digite 0 para voltar): ")
        if nome == '0':
            return
        for contato in agenda:
            if contato['Nome'] == nome:
                print("Nome encontrado:")
                print(contato)
                return
        print("Nome não encontrado.")

def excluir_nome(agenda):
    while True:
        nome = input("Digite o nome a ser excluído (ou digite 0 para voltar): ")
        if nome == '0':
            return
        for contato in agenda:
            if contato['Nome'] == nome:
                agenda.remove(contato)
                print("Nome excluído com sucesso!")
                return
        print("Nome não encontrado.")

def listar_nomes(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        print("Lista de Nomes na Agenda:")
        for contato in agenda:
            print(contato)

def zerar_agenda(agenda):
    confirmacao = input("Tem certeza que deseja zerar a agenda? (S/N): ")
    if confirmacao.lower() == 's':
        agenda.clear()
        print("Agenda zerada com sucesso!")
    else:
        print("Operação cancelada.")

def desenvolvedores():
    print("Desenvolvedores do Programa:")
    print("Matrícula: 202310631 - Nome: Pedro Leal Primo Teixeira Coelho")
    print("Matrícula: 202313146 - Nome: Jeziel Luiz Monteiro Farani")

def agendas():
    agenda = []

    while True:
        print("#------------------------------------------------------#")
        print("#        A G E N D A   D E   E N D E R E Ç O S         #")
        print("#------------------------------------------------------#")
        print("# OPÇÕES                                               #")
        print("# 1 - CADASTRAR NOME                                   #")
        print("# 2 - CONSULTAR NOME                                   #")
        print("# 3 - EXCLUIR NOME                                     #")
        print("# 4 - LISTAR TODOS OS NOMES                            #")
        print("# 5 - ZERAR AGENDA                                     #")
        print("# 6 - DESENVOLVEDORES                                  #")
        print("# 7 - SAIR                                             #")
        print("#------------------------------------------------------#")

        opcao = input("DIGITE A OPÇÃO DESEJADA (1 A 7): ")

        if opcao == '1':
            cadastrar_nome(agenda)
        elif opcao == '2':
            consultar_nome(agenda)
        elif opcao == '3':
            excluir_nome(agenda)
        elif opcao == '4':
            listar_nomes(agenda)
        elif opcao == '5':
            zerar_agenda(agenda)
        elif opcao == '6':
            desenvolvedores()
        elif opcao == '7':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

agendas()
tarefas = []

def menu():
    print("\nMenu de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Marcar tarefa como concluída")
    print("5. Sair")    

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"tarefa": tarefa, "feito": False})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = " (Concluída)" if tarefa["feito"] else " (Pendente)"
            print(f"{i}. {tarefa['tarefa']}{status}")

def remover_tarefa():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    listar_tarefas()
    if tarefas:
        try:
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefa_removida = tarefas.pop(indice)
                print(f"Tarefa '{tarefa_removida['tarefa']}' removida com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")

def marcar_concluida():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return 
      
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["feito"] = True
            print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.") 

def __main__():
    while True:
        menu()
        opcao = input("Escolha uma opção (1/2/3/4/5): ")
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            remover_tarefa()
        elif opcao == '4':
            marcar_concluida()
        elif opcao == '5':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1/2/3/4/5).")
__main__()
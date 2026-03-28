tarefas = []

while True:
    print("\nMENU")
    print("1 - Adicionar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print("Adicionada!")

    elif opcao == "2":
        for i, t in enumerate(tarefas, start=1):
            print(f"{i}. {t}")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida")1
# Contatos iniciais de exemplo armazenados como uma lista de dicionários
lista_contatos = [
    {"id": "4002", "nome": "Moises", "atividade": "Estudante", "telefone": "21988465143"},
    {"id": "8922", "nome": "Duda", "atividade": "Estudante", "telefone": "2196446681"}
]


# Função para cadastrar um novo contato
def cadastrar_contato(id_contato):
    novo_contato = {
        "id": id_contato,
        "nome": input("Por favor, informe o nome do contato: ").strip(),
        "atividade": input("Por favor, informe a atividade/cargo do contato: ").strip(),
        "telefone": input("Por favor, informe o telefone do contato: ").strip()
    }
    lista_contatos.append(novo_contato.copy())
    print("Contato cadastrado com sucesso!\n")


# Função para consultar e exibir contatos
def consultar_contatos():
    while True:
        opcao = input(
            "\nEscolha a opção desejada:\n"
            "1. Consultar todos os contatos\n"
            "2. Consultar por ID\n"
            "3. Consultar por atividade/setor\n"
            "4. Retornar ao menu principal\n"
            "Opção: "
        ).strip()

        if opcao == "1":
            if not lista_contatos:
                print("Nenhum contato cadastrado.\n")
            for contato in lista_contatos:
                print(f"ID: {contato['id']}")
                print(f"Nome: {contato['nome']}")
                print(f"Atividade: {contato['atividade']}")
                print(f"Telefone: {contato['telefone']}\n")

        elif opcao == "2":
            busca_id = input("Por favor, informe o ID do contato: ").strip()
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == busca_id:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}\n")
                    encontrado = True
                    break
            if not encontrado:
                print("Nenhum contato encontrado com este ID.\n")

        elif opcao == "3":
            busca_atividade = input("Por favor, informe a atividade do contato: ").strip().lower()
            encontrado = False
            for contato in lista_contatos:
                if contato["atividade"].lower() == busca_atividade:
                    print(f"ID: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"Atividade: {contato['atividade']}")
                    print(f"Telefone: {contato['telefone']}\n")
                    encontrado = True
            if not encontrado:
                print("Nenhum contato encontrado para esta atividade.\n")

        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")


# Função para remover um contato por ID
def remover_contato():
    id_alvo = input("Por favor, informe o ID do contato a ser removido: ").strip()
    for i, contato in enumerate(lista_contatos):
        if contato["id"] == id_alvo:
            del lista_contatos[i]
            print("Contato removido com sucesso.\n")
            return
    print("Nenhum contato encontrado com este ID.\n")


# Loop do menu principal
while True:
    print("\nBem-vindo à Lista de Contatos de Maria Eduarda Gonçalves!")
    print("Escolha a opção desejada:")
    print("1. Cadastrar Contato\n2. Consultar Contato(s)\n3. Remover Contato\n4. Sair")
    escolha_menu = input("Opção: ").strip()

    if escolha_menu == "1":
        cadastrar_contato(input("ID do contato: ").strip())
    elif escolha_menu == "2":
        consultar_contatos()
    elif escolha_menu == "3":
        remover_contato()
    elif escolha_menu == "4":
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

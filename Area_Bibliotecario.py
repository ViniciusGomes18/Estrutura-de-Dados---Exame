from historico import LinkedList

def area_bibliotecario(biblioteca, historico):
    print("\n--- Login do Bibliotecário ---")

    cpf = input("Digite seu CPF: ").strip()
    senha_digitada = input("Digite sua senha: ").strip()

    bibliotecario = biblioteca.bibliotecarios.get(cpf)

    if not bibliotecario:
        print("CPF não encontrado. Acesso negado.")
        return

    senha_cadastrada = bibliotecario[2]
    if senha_digitada != senha_cadastrada:
        print("Senha incorreta! Acesso negado.")
        return

    while True:
        print("\n--- Área do Bibliotecário ---")
        print("1. Excluir Livro")
        print("2. Editar Contato do Leitor")
        print("3. Excluir Leitor")
        print("4. Histórico de Ações")
        print("5. Listar Leitores")
        print("6. Voltar")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            titulo = input("Digite o título do livro a ser excluído: ").strip()
            if titulo in biblioteca.livros:
                livro = biblioteca.livros[titulo]
                biblioteca.Excluir_Livro(titulo)
                historico.Adicionar(
                    "Exclusão de Livro",
                    f"Título: {livro[0]}, Autor: {livro[1]}",
                    "Livro removido"
                )
            else:
                print("Livro não encontrado.")

        elif escolha == "2":
            cpf_leitor = input("Digite o CPF do leitor: ").strip()
            leitor = biblioteca.leitores.get(cpf_leitor)
            if leitor:
                contato_antigo = (leitor.dados[3][0], leitor.dados[3][1])  # email, telefone
                biblioteca.Atualizar_Contato(cpf_leitor)
                contato_novo = (leitor.dados[3][0], leitor.dados[3][1])
                historico.Adicionar(
                    "Atualização de Contato",
                    f"Email: {contato_antigo[0]}, Telefone: {contato_antigo[1]}",
                    f"Email: {contato_novo[0]}, Telefone: {contato_novo[1]}"
                )
            else:
                print("Leitor não encontrado.")

        elif escolha == "3":
            cpf_leitor = input("Digite o CPF do leitor: ").strip()
            leitor = biblioteca.leitores.get(cpf_leitor)
            if leitor:
                nome = leitor.dados[0]
                contato = (leitor.dados[3][0], leitor.dados[3][1])  # email, telefone
                biblioteca.Excluir_Leitor(cpf_leitor)
                historico.Adicionar(
                    "Exclusão de Leitor",
                    f"Nome: {nome}, CPF: {cpf_leitor}, Contato: {contato}",
                    "Leitor removido"
                )
            else:
                print("Leitor não encontrado.")

        elif escolha == "4":
            print("\n--- Histórico de Ações ---")
            if historico.head is None:
                print("Nenhuma ação registrada.")
            else:
                for node in historico:
                    print(f"Ação: {node.acao}")
                    print(f"De: {node.dado_anterior}")
                    print(f"Para: {node.dado_novo}")
                    print("-" * 30)

        elif escolha == "5":
            print("\n--- Leitores Cadastrados ---")
            if not biblioteca.leitores:
                print("Nenhum leitor cadastrado.")
            else:
                for cpf, leitor in biblioteca.leitores.items():
                    nome = leitor.dados[0]
                    endereco = leitor.dados[1]
                    nascimento = leitor.dados[2]
                    email, telefone = leitor.dados[3]
                    print(f"CPF: {cpf}")
                    print(f"Nome: {nome}")
                    print(f"Endereço: {endereco}")
                    print(f"Data de Nascimento: {nascimento}")
                    print(f"Email: {email} | Telefone: {telefone}")
                    print("-" * 40)

        elif escolha == "6":
            break

        else:
            print("Opção inválida. Tente novamente.")

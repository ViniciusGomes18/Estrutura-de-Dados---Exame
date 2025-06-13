def Gerar_Carteirinha(leitor, cpf, emprestimos):
    nome = leitor.dados[0]
    email, telefone = leitor.dados[3]

    # Filtra os empréstimos do leitor com base no CPF
    emprestimos_do_leitor = [
        e for e in emprestimos
        if hasattr(e.leitor, 'dados') and e.leitor.dados[1] == cpf and e.ativo
    ]

    cart = [
        f"--- Carteirinha do Leitor ---",
        f"Nome: {nome}",
        f"CPF: {cpf}",
        f"E-mail: {email}",
        f"Telefone: {telefone}",
        "Livros emprestados:"
    ]

    if not emprestimos_do_leitor:
        cart.append("Nenhum livro emprestado.")
    else:
        for e in emprestimos_do_leitor:
            for titulo in e.livros:
                cart.append(f"- {titulo} (em {e.data_emprestimo})")

    return "\n".join(cart)
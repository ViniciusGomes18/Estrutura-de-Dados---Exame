from datetime import date, timedelta

class Emprestimo:
    def __init__(self, id_emprestimo: int, leitor: tuple, livros: list, dias_para_devolucao: int = 7):
        self.id_emprestimo = id_emprestimo
        self.leitor = leitor  # tupla: (nome, cpf, nascimento, [email, telefone])
        self.livros = livros
        self.data_emprestimo = date.today()
        self.data_devolucao = self.data_emprestimo + timedelta(days=dias_para_devolucao)
        self.devolvido = False
        self.ativo = True


    def Exibir_detalhes(self):
        detalhes = (
            f"ID Empréstimo: {self.id_emprestimo}\n"
            f"Leitor: {self.leitor[0]} | CPF: {self.leitor[1]} | Email: {self.leitor[3][0]}\n"
            f"Livros: {', '.join(self.livros)}\n"
            f"Data do Empréstimo: {self.data_emprestimo}\n"
            f"Data de Devolução: {self.data_devolucao}\n"
            f"Status: {'Devolvido' if self.devolvido else 'Em aberto'}"
        )
        return detalhes

    def Registrar_devolucao(self):

        if not self.devolvido:
            self.devolvido = True
            return "Devolução registrada com sucesso."
        else:
            return "Os livros já foram devolvidos."

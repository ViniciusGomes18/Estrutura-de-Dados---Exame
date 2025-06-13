from datetime import datetime
from carteirinha import Gerar_Carteirinha

class Leitor:
    def __init__(self, emprestimos):
        # Nome
        nome = input("Digite o nome: ")

        # CPF
        while True:
            cpf = input("Digite o CPF (somente números): ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("CPF inválido. Digite exatamente 11 números.")

        # Data de nascimento
        while True:
            try:
                data = input("Digite a data de nascimento (DD/MM/AAAA): ")
                data_nasc = datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")

        # E-mail
        while True:
            email = input("Digite o email: ")
            if "@" in email and "." in email:
                break
            print("Email inválido.")

        # Telefone
        while True:
            tel = input("Digite o telefone (somente números): ")
            if tel.isdigit() and len(tel) == 11:
                telefone = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
                break
            print("Telefone inválido. Digite exatamente 11 números.")

        # Tupla de dados
        self.dados = (nome, cpf, data_nasc, [email, telefone])

        self.carteirinha = Gerar_Carteirinha(self, cpf, emprestimos)

    def __str__(self):
        nome, cpf, data_nasc, contato = self.dados
        return (
            f"Nome: {nome} | CPF: {cpf} | "
            f"Nasc: {data_nasc} | E-mail: {contato[0]} | Fone: {contato[1]}"
        )

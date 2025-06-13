import re

class Bibliotecario:

    def __init__(self):
        nome = input("Digite o nome: ")

        while True:
            cpf = input("Digite o CPF (somente números): ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            else:
                print("CPF inválido. Digite exatamente 11 números.")

        while True:
            senha = input("Digite uma senha (mínimo 8 caracteres, com letras e números)\n A senha não poderá ser alterada após a criação do cadastro: ")
            if len(senha) >= 8 and re.search(r"[A-Za-z]", senha) and re.search(r"\d", senha):
                print("Senha válida cadastrada!")
                break
            else:
                print("Senha inválida. Certifique-se de que tenha pelo menos 8 caracteres e contenha letras e números.")

        while True:
            email = input("Digite o email: ")
            if "@" in email and "." in email:
                break
            else:
                print("Email inválido.")

        while True:
            tel = input("Digite o telefone (somente números): ")
            if tel.isdigit() and len(tel) == 11:
                telefone = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}"
                break
            else:
                print("Telefone inválido. Digite exatamente 11 números.")

        self.dados = (
            nome,
            cpf,
            senha,
            [email, telefone]
        )
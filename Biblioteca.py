import pickle
from Livro import Livro
from lista_espera import ListaEspera
from Emprestimo import Emprestimo
from Leitor import Leitor
from Bibliotecario import Bibliotecario
from carteirinha import Gerar_Carteirinha

class Biblioteca:

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.livros = {} #Armazena Estoque de Livros em Dict e Suas informações dentro de tuplas
        self.leitores = {} # Armazena Leitores em Dict e Suas informações dentro de tuplas
        self.emprestimos = []
        self.fila_reservas = {}
        self.devolucoes_recentes = []
        self.leitores_por_livro = {}
        self.bibliotecarios = {}
        self.carteirinhas = {}

    def Cadastrar_Bibliotecario(self):
        novo_bibliotecario = Bibliotecario()
        cpf = novo_bibliotecario.dados[1]
        if cpf in self.bibliotecarios:
            print(f"O Bibliotecario {novo_bibliotecario.dados[0]} já está cadastrado")
        else:
            self.bibliotecarios[cpf] = novo_bibliotecario.dados
            print(f"O Bibliotecario {novo_bibliotecario.dados[0]} foi cadastrado com sucesso")
            self.Salvar_Dados()

    def Cadastrar_Livro(self):
        novo_livro = Livro()
        titulo = novo_livro.dados[0]

        if titulo in self.livros:
            print(f"O livro '{titulo}' já está cadastrado")
        else:
            self.livros[titulo] = novo_livro.dados
            print(f"O livro '{titulo}' foi cadastrado com sucesso")
            self.Salvar_Dados()

    def Excluir_Livro(self, livro):
        if livro not in self.livros:
            print(f'O livro "{livro}" não existe no estoque')
            return

        fila = self.fila_reservas.get(livro)
        if fila and not fila.esta_vazia():
            print(f'Não é possível excluir o livro "{livro}", pois há leitores na fila de espera.')
            return

        if self.livros[livro][4][0] < self.livros[livro][4][1]:
            print(f'Não é possível excluir o livro "{livro}", pois ele está emprestado no momento.')
            return

        self.livros.pop(livro)
        self.fila_reservas.pop(livro, None)
        self.leitores_por_livro.pop(livro, None)

        print(f'O livro "{livro}" foi excluído com sucesso do estoque')
        self.Salvar_Dados()

    def Cadastrar_Leitor(self):
        novo_leitor = Leitor([])
        cpf = novo_leitor.dados[1]

        if cpf in self.leitores:
            print(f"O leitor {novo_leitor.dados[0]} já está cadastrado")
        else:
            self.leitores[cpf] = novo_leitor
            self.carteirinhas[cpf] = novo_leitor.carteirinha
            print(novo_leitor.carteirinha)

            print(f"O leitor {novo_leitor.dados[0]} foi cadastrado com sucesso")
            self.Salvar_Dados()

    def Excluir_Leitor(self, cpf):
        if cpf in self.leitores:
            nome = self.leitores[cpf].dados[0]
            self.leitores.pop(cpf)
            print(f"O leitor {nome} foi excluído com sucesso.")
            self.Salvar_Dados()
        else:
            print(f"O leitor com CPF {cpf} não existe no cadastro.")

    def Gerar_Carteirinha_Leitor(self, cpf):
        leitor = self.leitores.get(cpf)
        if leitor:
            carteirinha = Gerar_Carteirinha(leitor, cpf, self.emprestimos)
            print(carteirinha)
        else:
            print("Leitor não encontrado.")

    def Emprestar_Livro(self, titulo, cpf):
        try:
            leitor = self.leitores[cpf]
        except KeyError:
            print(f"Leitor com CPF {cpf} não está cadastrado.")
            return

        if titulo not in self.livros:
            print(f"O livro '{titulo}' não existe no sistema.")
            return

        if self.livros[titulo][4][0] > 0:
            self.livros[titulo][4][0] -= 1

            emprestimo = Emprestimo(
                id_emprestimo=len(self.emprestimos) + 1,
                leitor=leitor,
                livros=[titulo]
            )

            self.emprestimos.append(emprestimo)

            if titulo not in self.leitores_por_livro:
                self.leitores_por_livro[titulo] = set()
            self.leitores_por_livro[titulo].add(cpf)

            self.Salvar_Dados()
            print(f"O livro '{titulo}' foi emprestado para {leitor.dados[0]} com sucesso em {emprestimo.data_emprestimo}!")
        else:
            print(f"O livro '{titulo}' não está disponível no momento.")

            if titulo not in self.fila_reservas:
                self.fila_reservas[titulo] = ListaEspera()

            fila = self.fila_reservas[titulo]
            
            nomes_na_fila = fila.listar_espera()
            if leitor.dados[0] in nomes_na_fila:
                print(f"O leitor {leitor.dados[0]} já está na lista de espera para '{titulo}'.")
            else:
                fila.adicionar_leitor(leitor)
                print(f"O leitor {leitor.dados[0]} foi adicionado à lista de espera para '{titulo}'.")


    def Devolver_Livro(self, livro, leitor):
        if livro in self.livros:
            self.livros[livro][4][0] += 1
            for emprestimo in self.emprestimos:
                if livro in emprestimo.livros and emprestimo.leitor == leitor and emprestimo.ativo:
                    emprestimo.ativo = False
                    break
                self.Salvar_Dados()
                print(f'O livro {livro} foi devolvido com sucesso!')


    def Livros_Mais_Populares_Unicos(self):
        if not self.leitores_por_livro:
            print("Nenhum empréstimo foi registrado ainda.")
            return

        mais_popular = max(self.leitores_por_livro.items(), key=lambda item: len(item[1]))
        titulo, leitores_set = mais_popular
        print(f"O livro mais popular é '{titulo}' com {len(leitores_set)} leitores únicos.")

    def Atualizar_Contato(self, cpf):
        if cpf not in self.leitores:
            print("Leitor não encontrado.")
            return

        leitor = self.leitores[cpf]
        while True:
            print("\n1. Alterar Email")
            print("2. Alterar Telefone")
            print("3. Voltar")
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha == 1:
                    novo_email = input("Digite o novo email: ").strip()
                    leitor.dados[3][0] = novo_email
                    print("Email alterado com sucesso!")
                elif escolha == 2:
                    novo_telefone = input("Digite o novo telefone: ").strip()
                    leitor.dados[3][1] = novo_telefone
                    print("Telefone alterado com sucesso!")
                elif escolha == 3:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Apenas números inteiros são aceitos.")
        self.Salvar_Dados()

    def Salvar_Dados(self):
        with open("biblioteca.pkl", "wb") as f:
            pickle.dump(self, f)

import pickle
import os
from Biblioteca import Biblioteca
from Area_Bibliotecario import area_bibliotecario
from historico import LinkedList

historico = LinkedList()
bibliotecario = None

def Carregar_Biblioteca():
    if os.path.exists("biblioteca.pkl"):
        with open("biblioteca.pkl", "rb") as f:
            return pickle.load(f)
    else:
        return Biblioteca("Biblioteca Central", "Rua das Letras, 123")

def Exibir_Menu():
    print("\n" + "=" * 45)
    print("☺  SISTEMA DE BIBLIOTECA  ☺".center(45))
    print("=" * 45)
    print("1. Cadastrar Livro")
    print("2. Cadastrar Leitor")
    print("3. Cadastrar Bibliotecario")
    print("4. Emprestar Livro")
    print("5. Devolver Livro")
    print("6. Ver Livro Mais Popular (leitores únicos)")
    print("7. Carteirinha do Leitor")
    print("8. Área do Bibliotecario")
    print("9. Ver Lista de Espera de um Livro")
    print("10. Sair")
    print("=" * 45)

def Main():
    biblioteca = Carregar_Biblioteca()

    while True:
        Exibir_Menu()
        try:
            opcao = int(input("Escolha uma opção: ").strip())
            
            if opcao == 1:
                print("\nCadastro de Livro")
                biblioteca.Cadastrar_Livro()

            elif opcao == 2:
                print("\nCadastro de Leitor")
                biblioteca.Cadastrar_Leitor()
            
            elif opcao == 3:
                print("\nCadastro de Bibliotecario")
                biblioteca.Cadastrar_Bibliotecario()

            elif opcao == 4:
                print("\nEmpréstimo de Livro")
                titulo = input("Título do livro: ").strip()
                cpf = input("CPF do leitor: ").strip()
                biblioteca.Emprestar_Livro(titulo, cpf)

            elif opcao == 5:
                print("\nDevolução de Livro")
                titulo = input("Título do livro a devolver: ").strip()
                cpf = input("CPF do leitor: ").strip()
                biblioteca.Devolver_Livro(titulo, cpf)

            elif opcao == 6:
                print("\nLivro mais popular por leitores únicos:")
                biblioteca.Livros_Mais_Populares_Unicos()

            elif opcao == 7:
                print("\nCarteirinha do Leitor")
                cpf = input("Digite o CPF do leitor: ").strip()
                biblioteca.Gerar_Carteirinha_Leitor(cpf)

            elif opcao == 8:
                if biblioteca.bibliotecarios is None:
                    print("Nenhum bibliotecário cadastrado ainda.")
                else:
                    area_bibliotecario(biblioteca, historico)

            elif opcao == 9:
                print("\nLista de Espera por Livro")
                titulo = input("Digite o título do livro: ").strip()
                if titulo in biblioteca.fila_reservas:
                    fila = biblioteca.fila_reservas[titulo]
                    fila.listar_espera()
                else:
                    print("Nenhuma fila de espera encontrada para este título.")

            elif opcao == 10:
                print("\nAté logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")
        

# Executa o programa
if __name__ == "__main__":
    Main()
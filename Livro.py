class Livro:
    def __init__(self):
        self.titulo = input('Digite o Título do livro: ')
        self.autor = input('Digite o Nome do Autor: ')
        
        while True:
            try:
                self.paginas = int(input('Total de Páginas: '))
                if self.paginas <= 0:
                    print("Erro: o número de páginas deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Erro: digite um número inteiro válido para as páginas.")

        while True:
            self.categoria = str(input('Categoria (ex: Ficção, Ação, Suspense...): ')).strip()
            if self.categoria == "":
                print("Erro: a categoria não pode estar vazia.")
            elif any(char.isdigit() for char in self.categoria):
                print("Erro: a categoria não pode conter números.")
            else:
                break

        while True:
            try:
                self.quantidade = int(input('Quantos livros você quer adicionar à biblioteca?: '))
                if self.quantidade <= 0:
                    print("Erro: a quantidade deve ser maior que 0.")
                else:
                    break
            except ValueError:
                print("Erro: digite um número inteiro válido.")

        self.dados = (
            self.titulo,
            self.autor,
            self.paginas,
            self.categoria,
            [self.quantidade] #Separa a quantidade em uma lista para ser iterável
        )

class No:
    def __init__(self, leitor):
        self.leitor = leitor
        self.proximo = None

class ListaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_leitor(self, leitor):
        novo = No(leitor)
        if self.fim:
            self.fim.proximo = novo
        else:
            self.inicio = novo
        self.fim = novo

    def remover_leitor(self):
        if self.inicio:
            leitor = self.inicio.leitor
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            return leitor
        return None

    def esta_vazia(self):
        return self.inicio is None

    def listar_espera(self):
        leitores = []
        atual = self.inicio
        while atual:
            leitores.append(atual.leitor.dados[0])
            atual = atual.proximo
        return leitores

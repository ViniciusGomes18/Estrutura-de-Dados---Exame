class Node:
    def __init__(self, acao, dado_anterior, dado_novo):
        self.acao = acao
        self.dado_anterior = dado_anterior
        self.dado_novo = dado_novo
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def Adicionar(self, acao, dado_anterior, dado_novo):
        novo_node = Node(acao, dado_anterior, dado_novo)
        if self.head is None:
            self.head = self.tail = novo_node
        else:
            self.tail.proximo = novo_node
            self.tail = novo_node

    def __iter__(self):
        atual = self.head
        while atual:
            yield atual
            atual = atual.proximo
Sistema de Biblioteca - Projeto P2 - Estrutura de Dados

# Integrantes:
- João Pedro Pereira Guerra - 2006484
- Gabriel Fante Javarotti - 1990554
- Vinicius da Silva Gomes - 2010424


# Como executar o sistema
 Para rodar o sistema, é só seguir os passos abaixo:

1. Clone o repositório do GitHub no seu computador.
2. Abra o terminal e copie e cole o cominho da pasta onde estão os arquivos:
cd "caminho do arquivo";

    OU SE PREFIRIR

Clique com o botão direito do mouse na pasta dos arquivos -> Abrir no Terminal

3. Depois, execute o programa principal:
python main.py

O sistema vai criar um arquivo chamado `biblioteca.pkl`, onde ele salva todos os dados (livros, leitores, histórico, etc). Na próxima vez que rodar, ele irá manter os dados adicionados e alterados salvos.

---

# Sobre o projeto

Este projeto simula uma biblioteca simples, com menu interativo no terminal. A ideia foi colocar em prática o que aprendemos de estruturas de dados em Python, usando listas, tuplas, sets, dicionários e lista encadeada.

# O que o sistema faz:

- Cadastra livros com título, autor, categoria e número de páginas
- Cadastra leitores com nome, CPF e data de nascimento, email e telefone
- Faz empréstimo e devolução de livros
- Gera carteirinhas dos leitores
- Mostra o livro mais popular (com base em quantos leitores diferentes pegaram)
- Mostra um histórico das ações realizadas pelo bibliotecario

As ações são todas feitas através de um menu simples, direto no terminal.

---

# Explicação das principais funções

- Cadastro de Livro
O usuário informa os dados do livro. Se for um título que já existe, ele só aumenta a quantidade. Caso contrário, cadastra como novo. Cada Livro fica armazenado dentro de um Dict, onde a chave é o título.

- Cadastro de Leitor
O sistema pede nome, CPF (com validação de 11 dígitos) e data de nascimento (Formato DD/MM/AAAA). Cada leitor fica salvo no Dicionario com seu CPF como chave.

- Empréstimo e Devolução
Na hora do empréstimo, o sistema verifica se o livro está disponível. Se estiver, a unidade do livro é retirada do estoque, quando o leitor devolve, o livro volta para o estoque.

- Livro mais popular
O sistema mostra qual livro foi mais emprestado para leitores diferentes, usando um `set` para contar CPFs únicos.

# Histórico de Ações do Bibliotecario
Todas as ações feitas no sistema vão para uma lista encadeada, que pode ser exibida depois.

---

# Estruturas de dados usadas e por quê

- Dicionário
Usamos dicionários para guardar os livros e os leitores:
- `self.livros[titulo] = Livro(...)`
- `self.leitores[cpf] = Leitor(...)`
**Motivo:** 
Porque facilita muito o acesso e a busca por título ou CPF.

---

# Lista
Usamos listas normais para armazenar os empréstimos e devoluções recentes. Também usamos listas para percorrer livros ou leitores cadastrados e para armazenar dados mutáveis(email, telefone(para Leitores), quantidade(para Livros)).
**Motivo:** 
Porque é simples de usar e ideal quando a ordem importa.

---

# Lista Encadeada
Criamos uma estrutura de lista encadeada com classes `No` e `ListaEncadeada`. Cada vez que uma ação acontece, ela é adicionada ao histórico
**Motivo:** 
Foi uma forma de aplicar o conteúdo teórico, e também porque permite adicionar itens no início com facilidade.


Para funcionalidade extra também foi utlizado LinkedList, Onde foi usado para adicionar leitores em espera de um livro que foi emprestado para outro leitor.
---

# Tupla
Alguns dados como os contatos dos leitores e dados fixos são guardados em tuplas.
**Motivo:** 
Tuplas são imutáveis e boas para guardar informações que não vão mudar.

---

# Set
Para saber o livro mais popular, usamos um conjunto (`set`) para armazenar os CPFs dos leitores que já pegaram aquele livro.
**Motivo:** 
Porque o `set` não deixa ter elementos repetidos, então conseguimos contar quantos leitores únicos pegaram cada livro.

---

# Armazenamento dos dados

Todos os dados da biblioteca ficam salvos em um arquivo chamado `biblioteca.pkl`, usando o módulo `pickle` do Python.

A gente tentou usar JSON no começo, mas descobrimos que ele não armazena tuplas do jeito certo — ele transforma tudo em lista ou dict. Como usamos tuplas para representar dados imutáveis (como as informações do leitor e livros), isso acabava bagunçando a estrutura ao salvar e depois carregar os dados.

Por isso, escolhemos o `pickle`, que consegue armazenar tudo exatamente como está, inclusive objetos de classe, listas encadeadas e tuplas.

Sempre que o sistema é iniciado, ele tenta carregar os dados salvos. Quando o usuário faz alguma ação, como cadastrar ou emprestar um livro, o sistema salva tudo automaticamente nesse arquivo.

Assim, mesmo fechando e abrindo o programa, os dados continuam lá.

---

# Considerações finais

Esse trabalho foi desenvolvido como projeto final do 3º termo da materia  de Estrutura de Dados.

Nosso objetivo principal foi aplicar as estruturas que estudamos na prática. Tentamos fazer algo funcional, que simulasse um sistema real de biblioteca, mas com foco no uso das estruturas certas para cada situação.

Fizemos o nosso melhor para realizar oque foi pedido nas instruções do projeto de forma clara e concisa, o projeto pode ter melhorias, como armazenar os dados em banco de dados, mas esperamos que dessa forma esteja atendendo todos os requisitos.
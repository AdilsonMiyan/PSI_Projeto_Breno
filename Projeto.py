#Adilson Miyan, Bernardo Carvalho, Victor Hnatouf, 11ºGPSIA, L2444, L2447, L2497

import tkinter as tk
from tkinter import messagebox, simpledialog

class Filme:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min) - Classificação: {self.classificacao}+"

class Sessao:
    def __init__(self, filme, horario, assentos_disponiveis):
        self.filme = filme
        self.horario = horario
        self.assentos_disponiveis = assentos_disponiveis

    def __str__(self):
        return f"{self.filme.titulo} - {self.horario} - Assentos disponíveis: {self.assentos_disponiveis}"

    def vender_ingresso(self):
        if self.assentos_disponiveis > 0:
            self.assentos_disponiveis -= 1
            return True
        return False

class Cliente:
    def __init__(self, nome, nif):
        self.nome = nome
        self.nif = nif
        self.ingressos = []

    def comprar_ingresso(self, sessao):
        if sessao.vender_ingresso():
            self.ingressos.append(sessao)
            return True
        return False

class Cinema:
    def __init__(self):
        self.sessoes = []

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)

    def listar_sessoes(self):
        return self.sessoes

cinema = Cinema()
clientes = []

#-----------------------------------------------------Parte de Adicionar a Sessão do Filme----------------------------------------------------------------------------------------

def adicionar_sessao():
    titulo = simpledialog.askstring("Adicionar Filme", "Título do filme:")
    if not titulo:
        return
    duracao = simpledialog.askinteger("Adicionar Filme", "Duração (min):")
    classificacao = simpledialog.askinteger("Adicionar Filme", "Classificação etária:")
    horario = simpledialog.askstring("Adicionar Sessão", "Horário da sessão (ex: 20:30):")
    assentos = simpledialog.askinteger("Adicionar Sessão", "Assentos disponíveis:")

    filme = Filme(titulo, duracao, classificacao)
    sessao = Sessao(filme, horario, assentos)
    cinema.adicionar_sessao(sessao)
    messagebox.showinfo("Sucesso", "Sessão adicionada com sucesso!")

#-----------------------------------------------------Parte de Cadastrar o Cliente----------------------------------------------------------------------------------------


def cadastrar_cliente():
    nome = simpledialog.askstring("Cadastrar Cliente", "Nome do cliente:")
    nif = simpledialog.askstring("Cadastrar Cliente", "NIF do cliente:")
    cliente = Cliente(nome, nif)
    clientes.append(cliente)
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    
#-----------------------------------------------------Parte de Comprar os Ingressos----------------------------------------------------------------------------------------


def comprar_ingresso():
    if not clientes or not cinema.sessoes:
        messagebox.showwarning("Aviso", "É necessário ter clientes e sessões cadastradas.")
        return

    nomes_clientes = [cliente.nome for cliente in clientes]
    nome_escolhido = simpledialog.askstring("Comprar Ingresso", f"Clientes disponíveis:\n{', '.join(nomes_clientes)}\nDigite o nome:")
    cliente = next((c for c in clientes if c.nome == nome_escolhido), None)
    if not cliente:
        messagebox.showerror("Erro", "Cliente não encontrado.")
        return

    lista_sessoes = cinema.listar_sessoes()
    opcoes = "\n".join([f"{i+1}. {s}" for i, s in enumerate(lista_sessoes)])
    escolha = simpledialog.askinteger("Escolher Sessão", f"Sessões disponíveis:\n{opcoes}\nDigite o número da sessão:")
    if escolha is None or escolha < 1 or escolha > len(lista_sessoes):
        return

    sessao = lista_sessoes[escolha - 1]
    if cliente.comprar_ingresso(sessao):
        messagebox.showinfo("Sucesso", f"Ingresso comprado para {sessao.filme.titulo} às {sessao.horario}")
    else:
        messagebox.showwarning("Erro", "Sessão lotada!")

#-----------------------------------------------------Parte de Mostrar os Ingressos----------------------------------------------------------------------------------------


def mostrar_ingressos():
    if not clientes:
        messagebox.showinfo("Informação", "Nenhum cliente cadastrado.")
        return

    nomes_clientes = [cliente.nome for cliente in clientes]
    nome_escolhido = simpledialog.askstring("Ingressos", f"Clientes:\n{', '.join(nomes_clientes)}\nDigite o nome:")
    cliente = next((c for c in clientes if c.nome == nome_escolhido), None)
    if not cliente:
        messagebox.showerror("Erro", "Cliente não encontrado.")
        return

    if not cliente.ingressos:
        messagebox.showinfo("Ingressos", "Nenhum ingresso comprado.")
    else:
        ingressos = "\n".join([f"{s.filme.titulo} às {s.horario}" for s in cliente.ingressos])
        messagebox.showinfo("Ingressos", f"Ingressos de {cliente.nome}:\n{ingressos}")

#-----------------------------------------------------Parte de Listar as Sessões de Cinema----------------------------------------------------------------------------------------


def listar_sessoes():
    if not cinema.sessoes:
        messagebox.showinfo("Sessões", "Nenhuma sessão disponível.")
    else:
        sessoes = "\n".join(str(sessao) for sessao in cinema.sessoes)
        messagebox.showinfo("Sessões Disponíveis", sessoes)

janela = tk.Tk()
janela.title("Sistema de Cinema")
janela.geometry("300x300")

tk.Label(janela, text="Menu Cinema", font=("Arial", 16)).pack(pady=10)

tk.Button(janela, text="Adicionar Filme e Sessão", command=adicionar_sessao).pack(pady=5)
tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente).pack(pady=5)
tk.Button(janela, text="Comprar Ingresso", command=comprar_ingresso).pack(pady=5)
tk.Button(janela, text="Mostrar Ingressos", command=mostrar_ingressos).pack(pady=5)
tk.Button(janela, text="Listar Sessões", command=listar_sessoes).pack(pady=5)
tk.Button(janela, text="Sair", command=janela.destroy).pack(pady=20)

janela.mainloop()

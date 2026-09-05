import json
import tkinter as tk



class Usuario:

  def __init__(self):
    try:
      with open("Projeto/Usuarios.json", "r") as arquivo:
        self.usuarios = json.load(arquivo)
    except FileNotFoundError:
      self.usuarios = {}

  def adicionar_usuario(self, nome, senha, saldo=0):
    self.usuarios[nome] = {"senha": senha, "saldo": saldo}

  def salvar(self):
    with open("Projeto/Usuarios.json", "w") as arquivo:
      json.dump(self.usuarios, arquivo, indent=2)



janela = tk.Tk()
janela.title("Apex")
janela.geometry("600x600")
janela.configure(bg="#0B0E14")


usuario_logado = ""


pagina_login = tk.Frame(janela, bg="#0B0E14")
pagina_login.pack(fill="both", expand=True)

tk.Label(
    pagina_login,
    text="Bem-vindo ao Apex",
    font=("Arial", 16, "bold"),
    bg="#0B0E14",
    fg="white",
).pack(pady=15)

tk.Label(
    pagina_login, text="Usuário", font=("Arial", 12), bg="#0B0E14", fg="white"
).pack(pady=2)
usuario_entry = tk.Entry(
    pagina_login,
    font=("Arial", 12),
    bg="#1C1F26",
    fg="white",
    insertbackground="white",
)
usuario_entry.pack(pady=5)

tk.Label(
    pagina_login, text="Senha", font=("Arial", 12), bg="#0B0E14", fg="white"
).pack(pady=2)
senha_entry = tk.Entry(
    pagina_login,
    font=("Arial", 12),
    show="*",
    bg="#1C1F26",
    fg="white",
    insertbackground="white",
)
senha_entry.pack(pady=5)

mensagem_label = tk.Label(
    pagina_login, text="", font=("Arial", 11), bg="#0B0E14"
)
mensagem_label.pack(pady=5)

tk.Button(
    pagina_login,
    text="Entrar",
    font=("Arial", 12, "bold"),
    command=lambda: login(usuario_entry.get(), senha_entry.get()),
    bg="#1C1F26",
    fg="white",
).pack(pady=10)

tk.Button(
    pagina_login,
    text="Cadastrar",
    font=("Arial", 12, "bold"),
    command=lambda: cadastrar_usuario(usuario_entry.get(), senha_entry.get()),
    bg="#1C1F26",
    fg="white",
).pack(pady=5)


pagina_sistema = tk.Frame(janela, bg="#0B0E14")

boas_vindas_label = tk.Label(
    pagina_sistema, text="", font=("Arial", 14), bg="#0B0E14", fg="white"
)
boas_vindas_label.pack(pady=10)

saldo_label = tk.Label(
    pagina_sistema,
    text="Saldo: R$ 0.00",
    font=("Arial", 14, "bold"),
    bg="#013220",
    fg="white",
)
saldo_label.pack(pady=10)

tk.Button(
    pagina_sistema,
    text="Sacar",
    font=("Arial", 12, "bold"),
    bg="#1C1F26",
    fg="white",
    command=lambda: alternar_campo_sacar(),
).pack(pady=10)

frame_saque = tk.Frame(pagina_sistema, bg="#0B0E14")

campo_sacar = tk.Entry(
    frame_saque,
    font=("Arial", 12),
    bg="#1C1F26",
    fg="white",
    insertbackground="white",
)
campo_sacar.pack(side="left", padx=5)

tk.Button(
    frame_saque,
    text="Confirmar Saque",
    font=("Arial", 10, "bold"),
    bg="#013220",
    fg="white",
    command=lambda: efetuar_saque(),
).pack(side="left")

btn_depositar = tk.Button(
    pagina_sistema,
    text="Depositar",
    font=("Arial", 12, "bold"),
    bg="#1C1F26",
    fg="white",
    command=lambda: alternar_campo_depositar(),
)
btn_depositar.pack(pady=10)

frame_deposito = tk.Frame(pagina_sistema, bg="#0B0E14")

campo_depositar = tk.Entry(
    frame_deposito,
    font=("Arial", 12),
    bg="#1C1F26",
    fg="white",
    insertbackground="white",
)
campo_depositar.pack(side="left", padx=5)

tk.Button(
    frame_deposito,
    text="Confirmar Depósito",
    font=("Arial", 10, "bold"),
    bg="#013220",
    fg="white",
    command=lambda: efetuar_deposito(),
).pack(side="left")

# Botão Sair
btn_sair = tk.Button(
    pagina_sistema,
    text="Sair",
    font=("Arial", 12, "bold"),
    command=lambda: sair(),
    bg="red",
    fg="white",
)
btn_sair.pack(pady=20)


def alternar_campo_sacar():
  frame_deposito.pack_forget()

  if frame_saque.winfo_viewable():
    frame_saque.pack_forget()
  else:
    frame_saque.pack(pady=10, before=btn_depositar)


def alternar_campo_depositar():
  frame_saque.pack_forget()

  if frame_deposito.winfo_viewable():
    frame_deposito.pack_forget()
  else:
    frame_deposito.pack(pady=10, before=btn_sair)


def efetuar_saque():
  global usuario_logado
  valor_saque_texto = campo_sacar.get().replace(",", ".")

  try:
    valor = float(valor_saque_texto)

    if valor <= 0:
      return

    u = Usuario()
    saldo_atual = u.usuarios[usuario_logado].get("saldo", 0)

    if round(valor, 2) <= round(saldo_atual, 2):
      novo_saldo = round(saldo_atual - valor, 2)

      if abs(novo_saldo) < 0.001:
        novo_saldo = 0.0

      u.usuarios[usuario_logado]["saldo"] = novo_saldo
      u.salvar()

      saldo_label.config(
          text=f"Saldo: R$ {u.usuarios[usuario_logado]['saldo']:.2f}"
      )
      campo_sacar.delete(0, tk.END)
      frame_saque.pack_forget()

  except ValueError:
    pass


def efetuar_deposito():
  global usuario_logado
  valor_deposito_texto = campo_depositar.get().replace(",", ".")

  try:
    valor = float(valor_deposito_texto)

    if valor <= 0:
      return

    u = Usuario()
    saldo_atual = u.usuarios[usuario_logado].get("saldo", 0)

    novo_saldo = round(saldo_atual + valor, 2)

    u.usuarios[usuario_logado]["saldo"] = novo_saldo
    u.salvar()

    saldo_label.config(
        text=f"Saldo: R$ {u.usuarios[usuario_logado]['saldo']:.2f}"
    )
    campo_depositar.delete(0, tk.END)
    frame_deposito.pack_forget()

  except ValueError:
    pass


def login(nome, senha):
  global usuario_logado
  usuario_obj = Usuario()

  if (
      nome in usuario_obj.usuarios
      and usuario_obj.usuarios[nome]["senha"] == senha
  ):
    usuario_logado = nome
    saldo = usuario_obj.usuarios[nome].get("saldo", 0)

    boas_vindas_label.config(text=f"Olá {nome}!")
    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

    pagina_login.pack_forget()
    pagina_sistema.pack(fill="both", expand=True)
  else:
    mensagem_label.config(text="Nome ou senha incorretos.", fg="red")


def cadastrar_usuario(usuario, senha):
  if usuario and senha:
    u = Usuario()
    u.adicionar_usuario(usuario, senha)
    u.salvar()
    mensagem_label.config(text="Usuário cadastrado com sucesso!", fg="green")
  else:
    mensagem_label.config(text="Preencha todos os campos.", fg="red")


def sair():
  frame_saque.pack_forget()
  frame_deposito.pack_forget()
  pagina_sistema.pack_forget()
  pagina_login.pack(fill="both", expand=True)


janela.mainloop()
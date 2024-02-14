import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import secrets
import string

class GeradorSenhas:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Gerador de Senhas")

        self.comprimento_var = StringVar(value="12")
        self.senha_var = StringVar(value="")

        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.janela, text="Comprimento da Senha:").grid(row=0, column=0, padx=10, pady=10)
        entry_comprimento = tk.Entry(self.janela, textvariable=self.comprimento_var, width=5)
        entry_comprimento.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(self.janela, text="Gerar Senha", command=self.gerar_senha).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Entry(self.janela, textvariable=self.senha_var, state="readonly", font=("Courier", 14), width=20).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self.janela, text="Copiar", command=self.copiar_senha).grid(row=3, column=0, columnspan=2, pady=10)

    def gerar_senha(self):
        try:
            comprimento = int(self.comprimento_var.get())
            if comprimento < 6:
                messagebox.showwarning("Aviso", "Comprimento da senha deve ser no mínimo 6.")
            else:
                caracteres = string.ascii_letters + string.digits + string.punctuation
                senha = ''.join(secrets.choice(caracteres) for _ in range(comprimento))
                self.senha_var.set(senha)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor inteiro para o comprimento da senha.")

    def copiar_senha(self):
        senha = self.senha_var.get()
        if senha:
            self.janela.clipboard_clear()
            self.janela.clipboard_append(senha)
            self.janela.update()
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")

    def iniciar_aplicacao(self):
        self.janela.mainloop()

if __name__ == "__main__":
    gerador = GeradorSenhas()
    gerador.iniciar_aplicacao()

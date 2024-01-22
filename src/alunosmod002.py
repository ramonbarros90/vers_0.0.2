import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Inicializando a janela principal
root = tk.Tk()
root.title("Sistema de cadastro de alunos")  

# Definindo o tamanho da janela como metade da largura e altura da tela
window_width = int(root.winfo_screenwidth() * 0.5)
window_height = int(root.winfo_screenheight() * 0.5)
root.geometry(f"{window_width}x{window_height}")

# Adicionando um título à janela
titulo = tk.Label(root, text="Sistema de cadastro de alunos", font=("Arial", 24))
titulo.grid(row=0, column=0, columnspan=2)  

# Inicializando um DataFrame para armazenar os dados dos alunos
df = pd.DataFrame(columns=["Nome", "Matrícula", "Nota1", "Nota2", "Nota3", "Média"])

# Função para adicionar um aluno
def add_student():
    global df
    nome = nome_entry.get()
    matricula = matricula_entry.get()
    nota1 = float(nota1_entry.get())
    nota2 = float(nota2_entry.get())
    nota3 = float(nota3_entry.get())
    media = (nota1 + nota2 + nota3) / 3
    new_row = pd.DataFrame({"Nome": [nome], "Matrícula": [matricula], "Nota1": [nota1], "Nota2": [nota2], "Nota3": [nota3], "Média": [media]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_excel("alunos.xlsx", index=False)
    messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
    nome_entry.delete(0, tk.END)
    matricula_entry.delete(0, tk.END)
    nota1_entry.delete(0, tk.END)
    nota2_entry.delete(0, tk.END)
    nota3_entry.delete(0, tk.END)

# Função para pesquisar um aluno
def search_student():
    global df
    matricula = matricula_entry.get()
    aluno = df[df["Matrícula"] == matricula]
    if aluno.empty:
        messagebox.showinfo("Erro", "Aluno não encontrado!")
    else:
        messagebox.showinfo("Sucesso", str(aluno))
    matricula_entry.delete(0, tk.END)
    
# Função para excluir um aluno
def delete_student():
    global df
    matricula = matricula_entry.get()
    df = df[df["Matrícula"] != matricula]
    df.to_excel("alunos.xlsx", index=False)
    messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
    matricula_entry.delete(0, tk.END)

# Aumentando o tamanho da fonte dos labels e entries
font_size = 20

# Criando os campos de entrada e os botões
nome_label = tk.Label(root, text="Nome", font=("Arial", font_size))
nome_entry = tk.Entry(root, font=("Arial", font_size), width=50)
matricula_label = tk.Label(root, text="Matrícula", font=("Arial", font_size))
matricula_entry = tk.Entry(root, font=("Arial", font_size), width=50)
nota1_label = tk.Label(root, text="Nota 1", font=("Arial", font_size))
nota1_entry = tk.Entry(root, font=("Arial", font_size), width=50)
nota2_label = tk.Label(root, text="Nota 2", font=("Arial", font_size))
nota2_entry = tk.Entry(root, font=("Arial", font_size), width=50)
nota3_label = tk.Label(root, text="Nota 3", font=("Arial", font_size))
nota3_entry = tk.Entry(root, font=("Arial", font_size), width=50)

# Aumentando o tamanho da fonte e o tamanho dos botões
button_font_size = 15
button_width = 20
button_height = 2
add_button = tk.Button(root, text="Adicionar Aluno", command=add_student, font=("Arial", button_font_size), width=button_width, height=button_height)
search_button = tk.Button(root, text="Pesquisar Aluno", command=search_student, font=("Arial", button_font_size), width=button_width, height=button_height)
delete_button = tk.Button(root, text="Excluir Aluno", command=delete_student, font=("Arial", button_font_size), width=button_width, height=button_height)

# Posicionando os elementos na janela
nome_label.grid(row=1, column=0)
nome_entry.grid(row=1, column=1)
matricula_label.grid(row=2, column=0)
matricula_entry.grid(row=2, column=1)
nota1_label.grid(row=3, column=0)
nota1_entry.grid(row=3, column=1)
nota2_label.grid(row=4, column=0)
nota2_entry.grid(row=4, column=1)
nota3_label.grid(row=5, column=0)
nota3_entry.grid(row=5, column=1)
add_button.grid(row=6, column=0, columnspan=2)
search_button.grid(row=7, column=0, columnspan=2)
delete_button.grid(row=8, column=0, columnspan=2)

# Iniciando o loop principal
root.mainloop()

import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

def mostrar_imagem_excecoes(event):
    """Abre uma nova janela (Toplevel) e exibe a imagem dentro dela."""
    # Cria uma nova janela
    top = Toplevel()
    top.title("Instruções de importação")

    # Carrega e redimensiona a imagem
    img = Image.open("C:/Users/normady/Desktop/GIT/automacao_txt_sped_contabil/imagem_excecoes.png")  # Substitua pelo caminho correto
    img = img.resize((300, 300))  # Redimensiona para ajustar à janela
    img_tk = ImageTk.PhotoImage(img)

    # Cria um Label na nova janela para exibir a imagem
    label_image = tk.Label(top, image=img_tk)
    label_image.image = img_tk  # Mantém a referência da imagem
    label_image.pack(pady=10)
    
def mostrar_imagem_vl_st(event):
    """Abre uma nova janela (Toplevel) e exibe a imagem dentro dela."""
    # Cria uma nova janela
    top = Toplevel()
    top.title("Instruções de importação")

    # Carrega e redimensiona a imagem
    img = Image.open("C:/Users/normady/Desktop/GIT/automacao_txt_sped_contabil/imagem_vl_st.png")  # Substitua pelo caminho correto
    img = img.resize((500, 400))  # Redimensiona para ajustar à janela
    img_tk = ImageTk.PhotoImage(img)

    # Cria um Label na nova janela para exibir a imagem
    label_image = tk.Label(top, image=img_tk)
    label_image.image = img_tk  # Mantém a referência da imagem
    label_image.pack(pady=10)
import os
import sys
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk

def get_resource_path(relative_path):
    """ Retorna o caminho absoluto, independentemente de estar empacotado ou não. """
    try:
        # Quando o programa está empacotado com PyInstaller
        base_path = sys._MEIPASS
    except AttributeError:
        # Durante o desenvolvimento (não empacotado)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def mostrar_imagem_excecoes(event):
    """Abre uma nova janela (Toplevel) e exibe a imagem dentro dela."""
    top = Toplevel()
    top.title("Instruções de importação")

    # Obter o caminho da imagem
    img_path = get_resource_path("imagem_excecoes.png")
    
    # Carrega e redimensiona a imagem
    img = Image.open(img_path)
    img = img.resize((300, 300))  # Redimensiona para ajustar à janela
    img_tk = ImageTk.PhotoImage(img)

    # Cria um Label na nova janela para exibir a imagem
    label_image = tk.Label(top, image=img_tk)
    label_image.image = img_tk  # Mantém a referência da imagem
    label_image.pack(pady=10)
    
def mostrar_imagem_vl_st(event):
    """Abre uma nova janela (Toplevel) e exibe a imagem dentro dela."""
    top = Toplevel()
    top.title("Instruções de importação")

    # Obter o caminho da imagem
    img_path = get_resource_path("imagem_vl_st.png")
    
    # Carrega e redimensiona a imagem
    img = Image.open(img_path)
    img = img.resize((500, 400))  # Redimensiona para ajustar à janela
    img_tk = ImageTk.PhotoImage(img)

    # Cria um Label na nova janela para exibir a imagem
    label_image = tk.Label(top, image=img_tk)
    label_image.image = img_tk  # Mantém a referência da imagem
    label_image.pack(pady=10)

# Aqui você poderia associar os eventos de clique aos botões ou labels que vão chamar essas funções.

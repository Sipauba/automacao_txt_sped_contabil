import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    
    global caminho_do_arquivo
    
    # Abre o diálogo de seleção de arquivo
    caminho_do_arquivo = filedialog.askopenfilename(title="Selecione um arquivo")
    
    # Retorna o caminho do arquivo selecionado
    return caminho_do_arquivo
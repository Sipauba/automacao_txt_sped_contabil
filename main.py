import tkinter as tk
from tkinter import ttk, Frame
from botao_localizar_atualizar import botao_localizar_atualizar
from label_assinatura import label_assinatura
from frame_excecoes import frame_excecoes
from frame_altera_vl_st import frame_altera_vl_st

root = tk.Tk()
root.title("Altera SPED Fiscal")
largura = 400
altura = 250
largura_screen = root.winfo_screenwidth()
altura_screen = root.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

def frame_aba_1(root):
    frame_aba_1 = Frame(root,
                        width=10,
                        height=10
                        )
    frame_aba_1.pack(expand=True, fill='both')
    
    botao_localizar_atualizar(frame_aba_1)
    label_assinatura(frame_aba_1)
    
    return frame_aba_1
    
def frame_aba_2(root):
    frame_aba_2 = Frame(root,
                        width=10,
                        height=10
                        )
    frame_aba_2.pack(expand=True, fill='both')
    
    frame_excecoes(frame_aba_2)
    label_assinatura(frame_aba_2)
    
    return frame_aba_2

def frame_aba_3(root):
    frame_aba_3 = Frame(root,
                        width=10,
                        height=10
                        )
    frame_aba_3.pack(expand=True, fill='both')
    
    frame_altera_vl_st(frame_aba_3)
    label_assinatura(frame_aba_3)
    
    return frame_aba_3
    
    
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')
notebook.add(frame_aba_1(notebook), text='Atualizar TXT')
notebook.add(frame_aba_2(notebook), text='Remover Exceções')
notebook.add(frame_aba_3(notebook), text='Altera VL ST')

root.mainloop()
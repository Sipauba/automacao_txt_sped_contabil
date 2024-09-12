from tkinter import Frame, Entry, Button
from seleciona_caminho_txt import seleciona_caminho_txt
from altera_txt import altera_txt

def frame_atualiza_txt(root):
    frame_atualiza_txt = Frame(root,
                           width=10,
                           height=10
                           )
    frame_atualiza_txt.place(x=20,y=55)
    
    global entry_importar_txt
    entry_importar_txt = Entry(frame_atualiza_txt, width=35)
    entry_importar_txt.grid(row=0, column=0)
    
    botao_importar_txt = Button(frame_atualiza_txt, text='IMPORTAR TXT', bg='silver',width=18, command=lambda:seleciona_caminho_txt(entry_importar_txt))
    botao_importar_txt.grid(row=0, column=1, padx=(10,0))
    
    botao_confirmar = Button(frame_atualiza_txt, text='EXECUTAR', bg='silver',command=lambda:altera_txt(entry_importar_txt,))
    botao_confirmar.grid(row=2, column=0, padx=(125,0), pady=(20,0))
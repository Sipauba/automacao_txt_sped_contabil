from tkinter import Frame, Label, Button, Entry, font
from seleciona_caminho_txt import seleciona_caminho_txt
from seleciona_caminho_excell import seleciona_caminho_excell
from executa_remocao import executa_remocao
from mostrar_imagens import mostrar_imagem_excecoes

def frame_excecoes(root):
    frame_excecoes = Frame(root,
                           width=10,
                           height=10
                           )
    frame_excecoes.place(x=20,y=55)
    
    global entry_importar_txt
    entry_importar_txt = Entry(frame_excecoes, width=35)
    entry_importar_txt.grid(row=0, column=0)
    
    botao_importar_txt = Button(frame_excecoes, text='IMPORTAR TXT', bg='silver',width=18, command=lambda:seleciona_caminho_txt(entry_importar_txt))
    botao_importar_txt.grid(row=0, column=1, padx=(10,0))
    
    entry_importar_excell = Entry(frame_excecoes, width=35)
    entry_importar_excell.grid(row=1, column=0)
    
    botao_importar_excell = Button(frame_excecoes, text='IMPORTAR PLANILHA',bg='silver',width=18, command=lambda:seleciona_caminho_excell(entry_importar_excell))
    botao_importar_excell.grid(row=1, column=1,padx=(10,0))
    
    botao_confirmar = Button(frame_excecoes, text='EXECUTAR', bg='silver',command=lambda:executa_remocao(entry_importar_txt,entry_importar_excell))
    botao_confirmar.grid(row=2, column=0, padx=(125,0), pady=(20,0))
    
    label_font = font.Font(underline=True)
    label_instrucoes = Label(frame_excecoes, text='?',font=label_font, fg="blue", cursor='hand2')
    label_instrucoes.grid(row=1, column=2, pady=(10,0))
    # Associar evento de clique à label de instrução
    label_instrucoes.bind("<Button-1>", mostrar_imagem_excecoes)

    
    return entry_importar_txt
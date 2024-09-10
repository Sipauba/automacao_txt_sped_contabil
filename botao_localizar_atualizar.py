from tkinter import Button
from altera_txt import altera_txt

def botao_localizar_atualizar(root):
    botao_localizar_atualizar = Button(root, text='LOCALIZAR ARQUIVO', width=20, height=1, bg='silver', command=altera_txt)
    botao_localizar_atualizar.place(x=120,y=80)

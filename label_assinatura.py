from tkinter import Label
import webbrowser

def abrir_site(event):
    url = "https://github.com/Sipauba"  # Substitua pelo site desejado
    webbrowser.open_new(url)

def label_assinatura(root):
    label_assinatura = Label(root, text = 'By Sipauba', fg = 'gray', cursor = 'hand2')
    label_assinatura.place(x=320,y=200 )
    label_assinatura.bind("<Button-1>", abrir_site)
    
    return label_assinatura
from tkinter import filedialog


def seleciona_caminho_txt(entry):
    # Abre o diálogo de seleção de arquivo
    caminho_arquivo_txt = filedialog.askopenfilename(title="Selecione um arquivo TXT")
    
    print(caminho_arquivo_txt)
    
    if caminho_arquivo_txt:
        # Atualiza o campo Entry com o caminho do arquivo selecionado
        entry.delete(0, 'end')  # Limpa o campo Entry
        entry.insert(0, caminho_arquivo_txt)  # Insere o caminho selecionado
        
    return caminho_arquivo_txt



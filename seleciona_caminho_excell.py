from tkinter import filedialog


def seleciona_caminho_excell(entry):
    # Abre o diálogo de seleção de arquivo
    caminho_arquivo_excell = filedialog.askopenfilename(title="Selecione um arquivo XLS ou XLSX")
    
    print(caminho_arquivo_excell)
    
    if caminho_arquivo_excell:
        # Atualiza o campo Entry com o caminho do arquivo selecionado
        entry.delete(0, 'end')  # Limpa o campo Entry
        entry.insert(0, caminho_arquivo_excell)  # Insere o caminho selecionado
        
    return caminho_arquivo_excell
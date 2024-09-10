import openpyxl
from tkinter import messagebox

def executa_remocao(caminho_txt, caminho_excel):
    
    caminho_txt = caminho_txt.get()
    caminho_excel = caminho_excel.get()
    
    # Leitura dos números da primeira coluna do Excel
    wb = openpyxl.load_workbook(caminho_excel)
    sheet = wb.active
    
    numeros_primeira_coluna = []
    
    # Pula a primeira linha e coleta todos os números da primeira coluna
    for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True):
        numeros_primeira_coluna.append(str(row[0]))  # Converte para string, caso não seja
    
    # Leitura e processamento do arquivo TXT
    with open(caminho_txt, 'r') as file:
        lines = file.readlines()
    
    # Lista para armazenar as novas linhas processadas
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Verifica se a linha começa com |E220|
        if line.startswith('|E220|'):
            parts = line.split('|')
            
            # Se o valor após o segundo | for CE100004, mantém a linha
            if parts[2] == 'CE100004':
                new_lines.append(line)
                i += 1
            else:
                # Se não for CE100004, verifica o número após o terceiro |
                numero_posicao_terceiro = parts[3]
                
                # Se o número estiver na lista de números do Excel, mantém a linha
                if numero_posicao_terceiro in numeros_primeira_coluna:
                    new_lines.append(line)
                    i += 1
                else:
                    # Caso contrário, remove as linhas até encontrar a próxima linha que começa com |E220| ou |E300|
                    i += 1
                    while i < len(lines):
                        if lines[i].startswith('|E220|') or lines[i].startswith('|E300|'):
                            break  # Para de remover linhas
                        i += 1
        else:
            # Adiciona as linhas que não começam com |E220| ao novo arquivo sem alteração
            new_lines.append(line)
            i += 1
    
    # Reescreve o arquivo TXT com as alterações
    with open(caminho_txt, 'w') as file:
        file.writelines(new_lines)
    
    print(f"Processamento concluído! O arquivo '{caminho_txt}' foi atualizado.")

    messagebox.showinfo('Sucesso', f"Processamento concluído! O arquivo '{caminho_txt}' foi atualizado.")
    
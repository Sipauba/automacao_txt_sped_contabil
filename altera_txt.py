from selecionar_arquivo import selecionar_arquivo
from tkinter import messagebox

def altera_txt(caminho_txt):
    # Usa a função para selecionar o arquivo
    
    #filename = selecionar_arquivo()
    caminho_txt = caminho_txt.get()

    if caminho_txt:
        # Lê o conteúdo do arquivo
        with open(caminho_txt, 'r') as file:
            lines = file.readlines()
        
        # Armazena as linhas processadas
        new_lines = []
        
        # Itera sobre as linhas do arquivo
        i = 0
        while i < len(lines):
            line = lines[i]
            
            if line.startswith('|E220|'):
                if i + 1 < len(lines):
                    next_line = lines[i + 2]
                    pipe_count = next_line.count('|')
                    
                    if pipe_count >= 10:
                        next_parts = next_line.split('|')
                        key_value = next_parts[10]
                        first_two_digits = key_value[:2]
                        
                        if first_two_digits == '23':
                            code_to_insert = 'CE100004'
                        else:
                            code_to_insert = 'CE100003'
                        
                        e220_parts = line.split('|', 2)
                        e220_parts[2] = code_to_insert + e220_parts[2]
                        line = '|'.join(e220_parts)
                        
                        number_to_insert = next_parts[6]
                        e220_parts = line.split('|')
                        e220_parts[3] += number_to_insert
                        line = '|'.join(e220_parts)
            
            new_lines.append(line)
            i += 1
        
        # Escreve as linhas processadas de volta para o arquivo
        with open(caminho_txt, 'w') as file:
            file.writelines(new_lines)
        
        # Exibe uma mensagem de sucesso ao usuário
        messagebox.showinfo("Sucesso", f"Processamento concluído! O arquivo '{caminho_txt}' foi atualizado.")
    else:
        # Exibe uma mensagem de aviso ao usuário
        messagebox.showwarning("Aviso", "Nenhum arquivo foi selecionado.")

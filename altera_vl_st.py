import openpyxl
from tkinter import messagebox

def altera_vl_st(caminho_txt, caminho_excel):
    
    caminho_txt = caminho_txt.get()
    caminho_excel = caminho_excel.get()
    
    # Carregar a planilha Excel
    wb = openpyxl.load_workbook(caminho_excel)
    sheet = wb.active

    # Dicionário para armazenar os dados da planilha Excel
    # Exemplo: {(coluna1, coluna2): valor_coluna4}
    dados_excel = {}

    # Ignora a primeira linha (cabeçalho) e coleta os dados das colunas 1, 2 e 4
    for row in sheet.iter_rows(min_row=2, values_only=True):
        coluna_1 = str(row[0])  # Primeira coluna
        coluna_2 = str(row[1])  # Segunda coluna
        valor_coluna_4 = row[3]  # Quarta coluna (mantém como número)

        # Trunca o valor da quarta coluna para ter 2 casas decimais e usa vírgula
        if isinstance(valor_coluna_4, (float, int)):
            valor_truncado = f"{int(valor_coluna_4 * 100) / 100:.2f}".replace('.', ',')  # Truncar para duas casas decimais
        else:
            valor_truncado = str(valor_coluna_4)  # Caso não seja número (tratamento de erro)

        # Armazena os dados em um dicionário, onde a chave é (coluna_1, coluna_2) e o valor é valor_truncado
        dados_excel[(coluna_1, coluna_2)] = valor_truncado

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
            partes_e220 = line.split('|')
            numero_apos_terceiro_pipe = partes_e220[3]  # Número após o terceiro caractere |

            # Soma total dos valores após o nono | nas linhas |E240| correspondentes
            total_soma = 0.0
            e220_index = len(new_lines)  # Armazena o índice da linha |E220| para atualizar depois
            new_lines.append(line)  # Adiciona a linha |E220| inicialmente sem modificar

            # Processa as linhas abaixo da linha |E220|
            i += 1
            while i < len(lines) and not lines[i].startswith('|E220|'):
                subline = lines[i]
                
                # Verifica se a linha começa com |E240|
                if subline.startswith('|E240|'):
                    partes_e240 = subline.split('|')
                    numero_apos_sexto_pipe = partes_e240[6]  # Número após o sexto caractere |
                    numero_apos_oitavo_pipe = partes_e240[8]  # Número após o oitavo caractere |

                    # Verifica se o número da linha |E240| corresponde ao da linha |E220|
                    if numero_apos_sexto_pipe == numero_apos_terceiro_pipe:
                        # Verifica se a combinação (coluna 1, coluna 2) está no dicionário do Excel
                        if (numero_apos_sexto_pipe, numero_apos_oitavo_pipe) in dados_excel:
                            # Substitui o valor após o nono | pelo valor truncado da quarta coluna do Excel
                            partes_e240[9] = dados_excel[(numero_apos_sexto_pipe, numero_apos_oitavo_pipe)]
                            subline = '|'.join(partes_e240)
                        
                        # Soma o valor após o nono |, verificando se é numérico
                        try:
                            total_soma += float(partes_e240[9].replace(',', '.'))  # Substitui vírgula por ponto para somar
                        except ValueError:
                            pass  # Se não for numérico, ignora a soma

                # Adiciona a linha |E240| (modificada ou não) ao arquivo novo
                new_lines.append(subline)
                i += 1

            # Após processar as linhas |E240|, atualiza o valor após o quarto | da linha |E220|
            partes_e220[4] = f"{total_soma:.2f}".replace('.', ',')  # Insere a soma e usa vírgula
            new_lines[e220_index] = '|'.join(partes_e220)  # Atualiza a linha |E220| no índice armazenado

        else:
            # Adiciona todas as outras linhas (não |E220|) sem modificação
            new_lines.append(line)
            i += 1

    # Reescreve o arquivo TXT com as alterações
    with open(caminho_txt, 'w') as file:
        file.writelines(new_lines)

    messagebox.showinfo("Sucesso", f"Processamento concluído! O arquivo '{caminho_txt}' foi atualizado.")
    
    print(f"Processamento concluído! O arquivo '{caminho_txt}' foi atualizado.")

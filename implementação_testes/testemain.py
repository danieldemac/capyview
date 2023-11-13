import tkinter as tk
from tkinter import Button, filedialog, Text
from funcao_html import gerar_php_Html
from funcao_model import gerar_php_model
from funcao_rota import gerar_rota
from funcao_js import gerar_js


tabela = 'modelos/tabela.php'

with open(tabela, 'r', encoding='UTF-8') as modelo:
    template = modelo.read()

# Encontrar o nome da tabela
nomeTabela = template.split("CREATE TABLE ")[1].split("\n")[0].strip()
nomeTabelaSingular = nomeTabela[:-1]

# Linhas da definição da tabela
linhas = template.splitlines()

# Inicializar a array bidimensional
valores = []

# Encontrar as linhas que contêm as definições das colunas
definicao_colunas = False
for linha in linhas:
    if "CREATE TABLE" in linha:
        definicao_colunas = True
        continue
    if definicao_colunas and linha != ")":
        partes = linha.strip().strip(",").split()
        if len(partes) >= 2:
            nome_coluna = partes[0]
            tipo_coluna = " ".join(partes[1:])
            valores.append([nome_coluna, tipo_coluna])

# Os tipos de variáveis
idVariables = ['bigint', 'bigserial', 'serial']
numVariables = ['bit', 'tinyint', 'smallint', 'int', 'numeric', 'decimal', 'real', 'float', 'smallmoney', 'money']
dateVariables = ['datetime', 'datetime2', 'smalldatetime', 'date', 'time', 'datetimeoffset', 'timestamp']
textVariables = ['char','"char"', 'varchar', 'text', 'nchar', 'nvarchar', 'ntext', 'binary', 'varbinary', 'image',
                'character']
otherVariables = ['sql_variant', 'uniqueidentifier', 'xml', 'cursor', 'table','rowversion', 'hierarchyid']

# Dicionário para armazenar variáveis separadas por tipo
variables_by_type = {
    "primaryKey": [],
    "Numeric": [],
    "Date": [],
    "Text": [],
    "Other": []
}

# Iterar pelos valores e classificar por tipo
for nome, tipo in valores:
    # Dividir o tipo de variável usando espaços como delimitador e pegar o primeiro elemento
    tipo = tipo.split()[0]

    if tipo in numVariables:
        variables_by_type["Numeric"].append(nome)
    elif tipo in dateVariables:
        variables_by_type["Date"].append(nome)
    elif tipo in idVariables:
        variables_by_type["primaryKey"].append(nome)
    elif tipo in textVariables:
        variables_by_type["Text"].append(nome)
    else:
        variables_by_type["Other"].append(nome)


# Transformar os resultados em strings com aspas simples
nome_Tabela_str = '"'+nomeTabela+'"'
id_semAspas = "".join([var for var in variables_by_type["primaryKey"]])
id_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["primaryKey"]])
numeric_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Numeric"]])
date_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Date"]])
text_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Text"]])
other_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Other"]])


def tudo():
    file_name_model = gerar_php_model(nomeTabelaSingular, nome_Tabela_str, id_semAspas, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str)
    file_name_html = gerar_php_Html(nomeTabelaSingular, nomeTabela)
    file_name_js = gerar_js(nomeTabelaSingular, nomeTabela)
    file_name_rota = gerar_rota(nomeTabelaSingular, nomeTabela)
    print(f"Arquivo '{file_name_html}' foi criado com sucesso.")
    print(" ")
    print(f"Arquivo '{file_name_model}' foi criado com sucesso.")
    print(" ")
    print(f"Arquivo '{file_name_js}' foi criado com sucesso.")
    print(" ")
    print(f"Arquivo '{file_name_rota}' foi criado com sucesso.")
    print(" ")
    



root = tk.Tk()
root.title("Capyview Beta")
selecionar_arquivo_button = Button(root, text="Criar", command=tudo(), bg="red")
selecionar_arquivo_button.grid(row=0, column=0)
resultado_text = Text(root)
resultado_text.grid(row=1, columnspan=4)
root.mainloop()




# Criação dos arquivos
# file_name_model = gerar_php_model(nomeTabelaSingular, nome_Tabela_str, id_semAspas, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str)
# file_name_html = gerar_php_Html(nomeTabelaSingular, nomeTabela)
# file_name_js = gerar_js(nomeTabelaSingular, nomeTabela)
# file_name_rota = gerar_rota(nomeTabelaSingular, nomeTabela)










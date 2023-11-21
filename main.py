from funcao_html import gerar_php_Html , criar_tabela_html
from funcao_model import gerar_php_model
from funcao_rota import gerar_rota
from funcao_js import gerar_js , criar_tabela_js
from funcao_query_model import escrever_query
from funcao_baixoModel import gerar_php_baixoModel


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

print("---------------------Criação das Views---------------------")
print(" ")
print("Nome da tabela:", nomeTabela)
print(" ")
print("Nome da tabela singular:",nomeTabelaSingular)
print(" ")
print("Valores das colunas:", valores)
print(" ")

# Os tipos de variáveis
idVariables = ['bigint', 'bigserial', 'serial']
numVariables = ['bit', 'tinyint', 'smallint', 'int', 'numeric', 'decimal', 'real', 'float', 'smallmoney', 'money','integer']
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

# Imprimir as variáveis separadas por tipo
print('Variável de ID:' + id_variables_str)
print(" ")
print("Variáveis Numéricas: " + numeric_variables_str)
print(" ")
print("Variáveis de Data: " + date_variables_str)
print(" ")
print("Variáveis de Texto: " + text_variables_str)
print(" ")
print("Outras Variáveis: " + other_variables_str)
print(" ")

#Variáveis funções
arrayTipos = variables_by_type["Text"] + variables_by_type["Numeric"]
arquivo_origem = 'modelos/modelo_query_model.php'
arquivo_destino = f'resultado/{nomeTabelaSingular}.php'
arquivo_saida_tabela = 'modelos/modelo_html_final.php'
arquivo_saida_tabela_js = 'modelos/modelo_js_final.js'

# Criação dos arquivos

#Model
file_name_model = gerar_php_model(nomeTabelaSingular, nome_Tabela_str, id_semAspas, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str, nomeTabela)
file_query_model = escrever_query(nomeTabelaSingular, arrayTipos)
file_baixoModel = gerar_php_baixoModel(nomeTabelaSingular, nomeTabela)
#HTML
file_name_html_tabela = criar_tabela_html(arrayTipos, arquivo_saida_tabela)
file_name_html = gerar_php_Html(nomeTabelaSingular, nomeTabela)
#JS
file_name_js_tabela = criar_tabela_js(arrayTipos, arquivo_saida_tabela_js)
file_name_js = gerar_js(nomeTabelaSingular, nomeTabela)
#ROTA
file_name_rota = gerar_rota(nomeTabelaSingular, nomeTabela)

print("---Criando Model---")
print(" ")
print(f"Arquivo '{file_name_model}' Primeira parte criada com sucesso.")
print(f"Arquivo '{file_query_model}' Adicionando as Querys com sucesso.")
print(f"Arquivo '{file_baixoModel}' foi finalizado com sucesso.")
print(" ")
print("---Criando HTML---")
print(" ")
print(f"Arquivo '{file_name_html_tabela }' gerado com sucesso.")
print(f"Usando '{file_name_html_tabela }' para criar arquivo final.")
print(f"Arquivo '{file_name_html}' foi criado com sucesso.")
print(" ")
print("---Criando JS---")
print(" ")
print(f"Arquivo '{file_name_js_tabela}' gerado com sucessor.")
print(f"Usando '{file_name_js_tabela }' para criar arquivo final.")
print(f"Arquivo '{file_name_js}' foi criado com sucesso.")
print(" ")
print("---Criando ROTA---")
print(" ")
print(f"Arquivo '{file_name_rota}' foi criado com sucesso.")
print(" ")



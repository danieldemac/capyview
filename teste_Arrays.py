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

def gerar_php_Html(singular, nome):
    modelo_file = f"modelos/modelo_index_blade.php"
    output_file = f"resultado/index.blade.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

   
    template = template.replace("{singular}", singular)
    template = template.replace("{plural}", nome)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

def gerar_js(singular, nome):
    modelo_file = f"modelos/modelo_js.js"
    output_file = f"resultado/{singular}.js"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

   
    template = template.replace("{singular}", singular)
    template = template.replace("{plural}", nome)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

def gerar_rota(singular, nome):
    modelo_file = f"modelos/modelo_rota.php"
    output_file = f"resultado/web.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

   
    template = template.replace("{singular}", singular)
    template = template.replace("{plural}", nome)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

def gerar_php_userDependent(nomeTabelaSingular, nomeTabela, num_Id, numero, texto, data):
    modelo_file = f"modelos/modelo_Model.php"
    output_file = f"resultado/{nomeTabelaSingular}.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

    template = template.replace("{nome}", nomeTabela)
    template = template.replace("{num_Id}", num_Id)
    template = template.replace("{Numeric}", numero)
    template = template.replace("{Text}", texto)
    template = template.replace("{Date}", data)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

# Criação dos arquivos
file_name_userDependent = gerar_php_userDependent(nomeTabelaSingular,nome_Tabela_str, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str)
file_name_html = gerar_php_Html(nomeTabelaSingular, nomeTabela)
file_name_js = gerar_js(nomeTabelaSingular, nomeTabela)
file_name_rota = gerar_rota(nomeTabelaSingular, nomeTabela)

print(f"Arquivo '{file_name_html}' foi criado com sucesso.")
print(" ")
print(f"Arquivo '{file_name_userDependent}' foi criado com sucesso.")
print(" ")
print(f"Arquivo '{file_name_js}' foi criado com sucesso.")
print(" ")
print(f"Arquivo '{file_name_rota}' foi criado com sucesso.")
print(" ")



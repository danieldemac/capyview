nomeTabela = 'user_dependents'
# Teste de separação variáveis
valores = [['id', 'bigint'], ['name', 'character varying(200)'], ['relationship', 'character varying(50)'],
           ['birth', 'date'], ['created_at', 'timestamp'], ['status', '"char"'],
           ['updated_at', 'timestamp'], ['deleted_at', 'timestamp']]

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

# Imprimir as variáveis separadas por tipo
print('Variável de ID:', variables_by_type["primaryKey"])
print("Variáveis Numéricas:", variables_by_type["Numeric"])
print("Variáveis de Data:", variables_by_type["Date"])
print("Variáveis de Texto:", variables_by_type["Text"])
print("Outras Variáveis:", variables_by_type["Other"])

# Transformar os resultados em strings com aspas simples
nome_Tabela_str = '"'+nomeTabela+'"'
id_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["primaryKey"]])
numeric_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Numeric"]])
date_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Date"]])
text_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Text"]])
other_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Other"]])

# Imprimir as variáveis separadas por tipo
print('Variável de ID:' + id_variables_str)
print("Variáveis Numéricas: " + numeric_variables_str)
print("Variáveis de Data: " + date_variables_str)
print("Variáveis de Texto: " + text_variables_str)
print("Outras Variáveis: " + other_variables_str)



def gerar_php_userDependent(nomeTabela, num_Id, numero, texto, data):
    modelo_file = f"modelos/modelo_User_Dependent.php"
    output_file = f"resultado/UserDependent.php"

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

file_name = gerar_php_userDependent(nome_Tabela_str, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str)
print(f"Arquivo '{file_name}' foi criado com sucesso.")
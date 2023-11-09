tabela = 'modelos/tabela.php'

with open(tabela, 'r', encoding='UTF-8') as modelo:
    template = modelo.read()

# Encontrar o nome da tabela
nome = template.split("CREATE TABLE ")[1].split("\n")[0].strip()

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

print("Nome da tabela:", nome)
print("Valores das colunas:", valores)

def gerar_php_Html(singular, nome):
    modelo_file = "modelos/modelo_index_blade.php"
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

# Os inputs
singular = input("Digite o nome SINGULAR: ")

file_name = gerar_php_Html(singular, nome)
print(f"Arquivo '{file_name}' foi criado com sucesso.")



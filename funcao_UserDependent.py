tabela = 'modelos/tabela.php'

with open(tabela, 'r', encoding='UTF-8') as modelo:
    template = modelo.read()

# Encontrar o nome da tabela
nome = template.split("CREATE TABLE ")[1].split("\n")[0].strip()

# Teste de linhas
linhas = template.splitlines()

# Definir os valores finais da array, excluindo "CREATE", "(", e ")"
valores = [temple.strip().split()[0] for temple in linhas if temple.strip() not in ["CREATE", "(", ")"]]

print("Nome da tabela:", nome)
print("Valores das colunas:", valores)

def gerar_php_userDependent(singular, nome):
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

file_name = gerar_php_userDependent(singular, nome)
print(f"Arquivo '{file_name}' foi criado com sucesso.")



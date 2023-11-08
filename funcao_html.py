def gerar_php_html(singular, plural):
    modelo_file = "modelos/modelo_index_blade.php"
    output_file = f"resultado/index.blade.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

   
    template = template.replace("{singular}", singular)
    template = template.replace("{plural}", plural)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

# Os inputs
SINGULAR = input("Digite o valor de SINGULAR: ")
PLURAL = input("Digite o valor de PLURAL: ")
file_name = gerar_php_html(SINGULAR, PLURAL)
print(f"Arquivo '{file_name}' foi criado com sucesso.")
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

def gerar_php_model(nomeTabelaSingular, nomeTabela, num_Id, numero, texto, data):
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
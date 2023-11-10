def gerar_php_model(nomeTabelaSingular, nomeTabela, num_Id, num_aspasId, numero, texto, data):
    modelo_file = f"modelos/modelo_Model.php"
    output_file = f"resultado/{nomeTabelaSingular}.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()

    template = template.replace("{nome}", nomeTabela)
    template = template.replace("{num_Id}", num_Id)
    template = template.replace("{num_aspasId}", num_aspasId)
    template = template.replace("{Numeric}", numero)
    template = template.replace("{Text}", texto)
    template = template.replace("{Date}", data)

    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file
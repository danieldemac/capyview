def gerar_php_model(nomeTabelaSingular, nomeTabelaStr, num_Id, num_aspasId, numeros, textos, datas, boolean, nomeTabela):
    modelo_file = f"modelos/modelo_altoModel.php"
    output_file = f"resultado/{nomeTabelaSingular}.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()
    template = template.replace("{nome}", nomeTabelaStr)
    template = template.replace("{nome_semAspas}", nomeTabela)
    template = template.replace("{num_Id}", num_Id)
    template = template.replace("{num_aspasId}", num_aspasId)
    template = template.replace("{Text}", textos)
    
    # Verifica se 'numeros' não está vazio antes de substituir
    if numeros:
        template = template.replace("{Numeric}", ',' + numeros)
    else:
        template = template.replace("{Numeric}", '')
    
    # Verifica se 'boolean' não está vazio antes de substituir
    if boolean:
        template = template.replace("{Booleano}", ',' + boolean)
    else:
        template = template.replace("{Booleano}", '')
    
    template = template.replace("{Date}", datas)
    
    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file




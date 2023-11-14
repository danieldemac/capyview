def substituir_texto(origem, destino, texto_substituir, substituicao):
    with open(origem, 'r') as arquivo_origem:
        conteudo = arquivo_origem.read()

    # Realiza a substituição no conteúdo lido do arquivo
    conteudo_modificado = conteudo.replace(texto_substituir, substituicao)

    with open(destino, 'w') as arquivo_destino:
        arquivo_destino.write(conteudo_modificado)

# Nome do arquivo de origem e destino
arquivo_origem = 'modelos/modelo_query_model.php'
arquivo_destino = f'resultado/{{nomeSingular}}.php'

# Texto a ser substituído e substituição desejada
texto_substituir = 'texto_a_substituir'
substituicao = '{query_list}'

# Chama a função para realizar a substituição
substituir_texto(arquivo_origem, arquivo_destino, texto_substituir, substituicao)
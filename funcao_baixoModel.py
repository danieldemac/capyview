def gerar_php_baixoModel(nomeSingular):
    # Caminho do arquivo de origem
    arquivo_origem = 'modelos/modelo_baixoModel.php'

    # Caminho do arquivo de destino
    caminho_destino = f'resultado/{nomeSingular}.php'

    # Lendo o conteúdo do arquivo de origem
    with open(arquivo_origem, 'r', encoding='utf-8') as arquivo_origem:
        conteudo = arquivo_origem.read()

    # Escrevendo o conteúdo lido no arquivo de destino (modo de adição)
    with open(caminho_destino, 'a', encoding='utf-8') as arquivo_destino:
        arquivo_destino.write(conteudo)
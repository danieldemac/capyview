#GERADOR DE HTML
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
#GERADOR DO JS
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
#GERADOR ROTA
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
#GERADOR MODEL
def gerar_php_model(nomeTabelaSingular, nomeTabela, num_Id, num_aspasId, numeros, textos, datas):
    modelo_file = f"modelos/modelo_altoModel.php"
    output_file = f"resultado/{nomeTabelaSingular}.php"

    # Lê o modelo
    with open(modelo_file, 'r', encoding='utf-8') as modelo:
        template = modelo.read()
    template = template.replace("{nome}", nomeTabela)
    template = template.replace("{num_Id}", num_Id)
    template = template.replace("{num_aspasId}", num_aspasId)
    template = template.replace("{Numeric}", ','+ numeros)
    template = template.replace("{Text}", textos)
    template = template.replace("{Date}", datas)
    
    # Escreve o conteúdo no novo arquivo
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(template)

    return output_file

def escrever_query(nomeSingular, valores):

    with open(f'resultado/{nomeSingular}.php', 'a+',  encoding='utf-8') as arquivo:
        if valores:
            arquivo.write(f" $query->where(DB::raw('lower({valores[0]})'),"+"LIKE"+","+"%"+".$search."+"%"+")\n")
            for valor in valores[1:]:
                arquivo.write(f"                                    ->orWhere(DB::raw('lower({valor})'),"+"LIKE"+","+"%"+".$search."+"%"+");\n")

        else:
            arquivo.write("Array vazia")

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

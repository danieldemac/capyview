def gerar_php_Html(singular, plural):
    modelo_file = f"modelos/modelo_html_final.php"
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

def criar_tabela_html(array, arquivo_saida):
    with open('modelos/modelo_html_1.php', 'r', encoding='utf-8') as modelo_1:
        modelo_1_content = modelo_1.read()

    with open('modelos/modelo_html_2.php', 'r', encoding='utf-8') as modelo_2:
        modelo_2_content = modelo_2.read()

    with open('modelos/modelo_html_3.php', 'r', encoding='utf-8') as modelo_3:
        modelo_3_content = modelo_3.read()

    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write(modelo_1_content)  # Escreve o conteúdo do modelo 1 original

        arquivo.write('\t\t\t\t\t\t<tr>\n')
        for item in array:
            arquivo.write(f'\t\t\t\t\t\t\t<th>{item.capitalize()}</th>\n')
        arquivo.write('\t\t\t\t\t\t</tr>\n')

        arquivo.write(modelo_2_content)  # Adiciona o conteúdo do modelo 2

        arquivo.write('''<form id="form-create-{singular}" enctype="multipart/form-data">\n''')
        for item in array:
            arquivo.write('''\t\t\t<div class="form-row">\n''')
            arquivo.write('''\t\t\t\t<div class="form-group mb-3">\n''')
            arquivo.write(f'''\t\t\t\t\t<label class="form-label" for="{item}">{item.capitalize().replace("_", " ")}{'*' if item != 'idade_filho' else ''}</label>\n''')
            arquivo.write(f'''\t\t\t\t\t<input type="text" class="form-control {'required' if item != 'idade_filho' else ''}" id="{item}">\n''')
            arquivo.write('''\t\t\t\t</div>\n''')
            arquivo.write('''\t\t\t</div>\n''')
        arquivo.write('''</form>''')

        arquivo.write(modelo_3_content)  # Adiciona o conteúdo do modelo 3 no final
    return arquivo_saida

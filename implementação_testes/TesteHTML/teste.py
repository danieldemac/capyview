def criar_form_html(array, arquivo_saida):
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write('''<form id="form-create-{singular}" enctype="multipart/form-data">\n''')
        
        for item in array:
            arquivo.write('''\t\t\t\t\t<div class="form-row">\n''')
            arquivo.write('''\t\t\t\t\t\t<div class="form-group mb-3">\n''')
            arquivo.write(f'''\t\t\t\t\t\t\t<label class="form-label" for="{item}">{item.capitalize().replace("_", " ")}{'*' if item != 'idade_filho' else ''}</label>\n''')
            arquivo.write(f'''\t\t\t\t\t\t\t<input type="text" class="form-control {'required' if item != 'idade_filho' else ''}" id="{item}">\n''')
            arquivo.write('''\t\t\t\t\t\t</div>\n''')
            arquivo.write('''\t\t\t\t\t</div>\n''')
        
        arquivo.write('''</form>''')

# Exemplo de uso com uma nova array
nova_array = ['name', 'relationship', 'status', 'idade_filho', 'novo_campo', 'outro_campo']
arquivo_saida = 'modelos/teste.php'

criar_form_html(nova_array, arquivo_saida)
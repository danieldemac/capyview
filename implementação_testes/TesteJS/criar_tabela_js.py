def criar_tabela_js(array, arquivo_saida):
    
    with open('modelos/modelo_js_1.js', 'r', encoding='utf-8') as modelo_1:
        modelo_1_content = modelo_1.read()

    with open('modelos/modelo_js_2.js', 'r', encoding='utf-8') as modelo_2:
        modelo_2_content = modelo_2.read()

    with open('modelos/modelo_js_3.js', 'r', encoding='utf-8') as modelo_3:
        modelo_3_content = modelo_3.read()
    
    with open('modelos/modelo_js_4.js', 'r', encoding='utf-8') as modelo_4:
        modelo_4_content = modelo_4.read()
    
    
    with open(arquivo_saida, 'w', encoding='utf-8') as arquivo:
        arquivo.write(modelo_1_content)  # Escreve o conteúdo do modelo 1 original

        for item in array:
            arquivo.write(f'''\t$('#{item}').val('');\n''')

        arquivo.write(modelo_2_content)  # Adiciona o conteúdo do modelo 2

        for item in array:
            arquivo.write(f'''\t\t{{ data: '{item}' }},\n''')
        
        arquivo.write(modelo_3_content)  # Adiciona o conteúdo do modelo 3

        for item in array:
            arquivo.write(f'''\t\t$('#{item}').val();\n''') 
        
        arquivo.write(modelo_4_content)  # Adiciona o conteúdo do modelo 3

arquivo_saida_tabela = 'modelos/modelo_js_final.js'
arrayTeste = ['name', 'relationship', 'status', 'idade_filho','Bora','Bill','LOL','Final']
teste = criar_tabela_js(arrayTeste, arquivo_saida_tabela)

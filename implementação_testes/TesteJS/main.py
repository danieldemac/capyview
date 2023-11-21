from funcao_js import gerar_js
from criar_tabela_js import criar_tabela_js
nome = 'TESTE'
nomes = 'TESTES'
arquivo_saida_tabela = 'modelos/modelo_js_final.js'
arrayTeste = ['name', 'relationship', 'status', 'idade_filho','Bora','Bill','LOL','Final']

teste2 = criar_tabela_js(arrayTeste, arquivo_saida_tabela)
teste = gerar_js(nome, nomes)

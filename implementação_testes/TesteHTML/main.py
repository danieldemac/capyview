from funcao_html import gerar_php_Html
from funcaoteste2 import criar_tabela_html
arquivo_saida_tabela = 'modelos/modelo_html_final.php'
arrayTeste = ['name', 'relationship', 'status', 'idade_filho']
singular = 'teste'
plural = 'testes'

teste = criar_tabela_html(arrayTeste, arquivo_saida_tabela)
teste2 = gerar_php_Html(singular, plural)

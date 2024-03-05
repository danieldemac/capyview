import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from funcao_html import gerar_php_Html , criar_tabela_html
from funcao_model import gerar_php_model
from funcao_rota import gerar_rota
from funcao_js import gerar_js , criar_tabela_js
from funcao_query_model import escrever_query
from funcao_baixoModel import gerar_php_baixoModel


def obter_texto_tabela():
    global tabela
    tabela = texto_tabela.get("1.0", "end-1c")
     # Fechar o programa
    inicio.destroy()  # Fechar a janela principal do Tkinter
    

def fechar():
    mostrar.destroy()
    
def fechar_janela():
    janela.destroy()
# Inicio do Programa
inicio = Tk()
inicio.title('CapyView - v.beta')
inicio.iconbitmap('capyview.ico')
inicio.geometry("500x400+200+100")

texto0 = Label(inicio, text='----> ')
texto0.grid(column=0, row=0)

texto1 = Label(inicio, text='Digite abaixo o comando criação ')
texto1.grid(column=1, row=0)

texto2 = Label(inicio, text=' <----')
texto2.grid(column=2, row=0)

texto_tabela = Text(inicio, height=15, width=50)
texto_tabela.grid(column=1, row=1)

botao_atualizar = Button(inicio, text="Atualizar Tabela", command=obter_texto_tabela)
botao_atualizar.grid(column=1, row=2)


inicio.mainloop()

#comando para procurar o arquivo
# tabela = filedialog.askopenfilename()



# Encontrar o nome da tabela
nomeTabela = tabela.split("CREATE TABLE ")[1].split("\n")[0].strip()
nomeTabelaSingular = nomeTabela[:-1]

# Linhas da definição da tabela
linhas = tabela.splitlines()

# Inicializar a array bidimensional
valores = []

# Encontrar as linhas que contêm as definições das colunas
definicao_colunas = False
for linha in linhas:
    if "CREATE TABLE" in linha:
        definicao_colunas = True
        continue
    if definicao_colunas and linha != ")":
        partes = linha.strip().strip(",").split()
        if len(partes) >= 2:
            nome_coluna = partes[0]
            # Juntar o tipo da coluna mantendo o espaço antes do parêntese
            tipo_coluna = " ".join(partes[1:]).replace('(', ' (')
            valores.append([nome_coluna, tipo_coluna])


print("---------------------Criação das Views---------------------")
print(" ")
print("Nome da tabela:", nomeTabela)
print(" ")
print("Nome da tabela singular:",nomeTabelaSingular)
print(" ")
print("Valores das colunas:", valores)
print(" ")

# Os tipos de variáveis
idVariables = ['bigint', 'bigserial', 'serial']
numVariables = ['bit','tinyint', 'smallint', 'int', 'numeric', 'decimal', 'real', 'float', 'smallmoney', 'money','integer']
booleanVariables = ['boolean', 'CHECKEXIST', 'BOOLEAN']
dateVariables = ['datetime', 'datetime2', 'smalldatetime', 'date', 'time', 'datetimeoffset', 'timestamp']
textVariables = ['char','"char"', 'varchar', 'text', 'nchar', 'nvarchar', 'ntext', 'binary', 'varbinary', 'image',
                'character']
otherVariables = ['sql_variant', 'uniqueidentifier', 'xml', 'cursor', 'table','rowversion', 'hierarchyid']

# Dicionário para armazenar variáveis separadas por tipo
variables_by_type = {
    "primaryKey": [],
    "Numeric": [],
    "Boolean":[],
    "Date": [],
    "Text": [],
    "Other": []
}

# Iterar pelos valores e classificar por tipo
for nome, tipo in valores:
    # Dividir o tipo de variável usando espaços como delimitador e pegar o primeiro elemento
    tipo = tipo.split()[0]

    if tipo in numVariables:
        variables_by_type["Numeric"].append(nome)
    elif tipo in dateVariables:
        variables_by_type["Date"].append(nome)
    elif tipo in idVariables:
        variables_by_type["primaryKey"].append(nome)
    elif tipo in booleanVariables:
        variables_by_type["Boolean"].append(nome)
    elif tipo in textVariables:
        variables_by_type["Text"].append(nome)
    else:
        variables_by_type["Other"].append(nome)


# Transformar os resultados em strings com aspas simples
nome_Tabela_str = '"'+nomeTabela+'"'
id_semAspas = "".join([var for var in variables_by_type["primaryKey"]])
id_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["primaryKey"]])
numeric_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Numeric"]])
date_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Date"]])
text_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Text"]])
boolean_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Boolean"]])
other_variables_str = ", ".join(["'" + var + "'" for var in variables_by_type["Other"]])

# Imprimir as variáveis separadas por tipo
print('Variável de ID:' + id_variables_str)
print(" ")  
print("Variáveis Numéricas: " + numeric_variables_str)
print(" ")
print("Variáveis de Data: " + date_variables_str)
print(" ")
print("Variáveis de Texto: " + text_variables_str)
print(" ")
print("Variáveis Boolean: " + boolean_variables_str)
print(" ")
print("Outras Variáveis: " + other_variables_str)
print(" ")

#Variáveis funções
arrayTipos = variables_by_type["Text"] + variables_by_type["Numeric"] + variables_by_type["Boolean"]
arquivo_origem = 'modelos/modelo_query_model.php'
arquivo_destino = f'resultado/{nomeTabelaSingular}.php'
arquivo_saida_tabela = 'modelos/modelo_html_final.php'
arquivo_saida_tabela_js = 'modelos/modelo_js_final.js'


resultados_text = f''' 
---------------------Criação das Views---------------------
Nome da tabela - {nomeTabela}
Nome da tabela singular - {nomeTabelaSingular}
Nome da tabela singular: {nomeTabelaSingular} 
Valores das colunas: {valores} 
Variável de ID: {id_variables_str} 
Variáveis Numéricas: {numeric_variables_str} 
Variáveis de Data: {date_variables_str} 
Variáveis de Texto: {text_variables_str} 
Variáveis Boolean: {boolean_variables_str}
Outras Variáveis: {other_variables_str}
'''


# Criar uma janela Tkinter
mostrar = Tk()
mostrar.title('CapyView - v.beta')
mostrar.iconbitmap('capyview.ico')

texto0 = Label(mostrar, text='----> ')
texto0.grid(column=0, row=0)

texto1 = Label(mostrar, text='Dados da tabela para geração dos Documentos ')
texto1.grid(column=1, row=0)

texto2 = Label(mostrar, text=' <----')
texto2.grid(column=2, row=0)

# Criar um widget Text para exibir o conteúdo
texto_resultados = Text(mostrar, height=20, width=100, padx=10, pady=10)
texto_resultados.grid(column=1, row=3, pady=10)

# Função para adicionar texto em negrito
def adicionar_negrito(texto):
    texto_resultados.tag_configure("negrito", font=("TkDefaultFont", 10, "bold"))
    texto_resultados.insert("end", texto, "negrito")

# Exibir o conteúdo da variável resultados_text no widget Text
adicionar_negrito("Nome da tabela - ")
texto_resultados.insert("end", f"{nomeTabela}\n")

adicionar_negrito("Nome da tabela singular - ")
texto_resultados.insert("end", f"{nomeTabelaSingular}\n")

adicionar_negrito("Nome da tabela singular: ")
texto_resultados.insert("end", f"{nomeTabelaSingular}\n")

adicionar_negrito("Valores das colunas: ")
texto_resultados.insert("end", f"{valores}\n")

adicionar_negrito("Variável de ID: ")
texto_resultados.insert("end", f"{id_variables_str}\n")

adicionar_negrito("Variáveis Numéricas: ")
texto_resultados.insert("end", f"{numeric_variables_str}\n")

adicionar_negrito("Variáveis de Data: ")
texto_resultados.insert("end", f"{date_variables_str}\n")

adicionar_negrito("Variáveis de Texto: ")
texto_resultados.insert("end", f"{text_variables_str}\n")

adicionar_negrito("Variáveis Boolean: ")
texto_resultados.insert("end", f"{boolean_variables_str}\n")

adicionar_negrito("Outras Variáveis: ")
texto_resultados.insert("end", f"{other_variables_str}\n")

# Desabilitar a edição no widget Text
texto_resultados.config(state="disabled")

botao_atualizar = Button(mostrar, text="Continuar", command=fechar)
botao_atualizar.grid(column=1, row=2)

mostrar.mainloop()


#Função para gerar tudo
def criar_tudo():
    # Model
    file_name_model = gerar_php_model(nomeTabelaSingular, nome_Tabela_str, id_semAspas, id_variables_str, numeric_variables_str, text_variables_str, date_variables_str, boolean_variables_str, nomeTabela)
    file_query_model = escrever_query(nomeTabelaSingular, arrayTipos)
    file_baixoModel = gerar_php_baixoModel(nomeTabelaSingular, nomeTabela)
    
    # HTML
    file_name_html_tabela = criar_tabela_html(arrayTipos, arquivo_saida_tabela)
    file_name_html = gerar_php_Html(nomeTabelaSingular, nomeTabela)
    
    # JS
    file_name_js_tabela = criar_tabela_js(arrayTipos, arquivo_saida_tabela_js)
    file_name_js = gerar_js(nomeTabelaSingular, nomeTabela)
    
    # ROTA
    file_name_rota = gerar_rota(nomeTabelaSingular, nomeTabela)

    #TEXTO
    texto = f'''
    ---Criando Model---
    
    Arquivo '{file_name_model}' Primeira parte criada com sucesso.
    Arquivo '{file_query_model}' Adicionando as Querys com sucesso.
    Arquivo '{file_baixoModel}' foi finalizado com sucesso.
    
    ---Criando HTML---
    
    Arquivo '{file_name_html_tabela }' gerado com sucesso.
    Usando '{file_name_html_tabela }' para criar arquivo final.
    Arquivo '{file_name_html}' foi criado com sucesso.
    
    ---Criando JS---
   
    Arquivo '{file_name_js_tabela}' gerado com sucessor.
    Usando '{file_name_js_tabela }' para criar arquivo final.
    Arquivo '{file_name_js}' foi criado com sucesso.
    
    ---Criando ROTA---
    
    Arquivo '{file_name_rota}' foi criado com sucesso.
    '''
    resultados['text'] = texto




#Criação da tela

janela = Tk()

# Define o título da janela
janela.title('CapyView - v.beta')

# Carrega o ícone e define para a janela
janela.iconbitmap('capyview.ico')
janela.geometry("500x600+200+100")

# Texto
texto1 = Label(janela, text='----> ')
texto1.grid(column=0, row=0)
texto3 = Label(janela, text='Clique no botão para gerar os Arquivos.')
texto3.grid(column=1, row=0, padx=10, pady=10)
texto2 = Label(janela, text=' <----')
texto2.grid(column=2, row=0)

# Botão
botao = Button(janela, text='Criar Arquivos', command=criar_tudo)
botao.grid(column=1, row=2)

# Informativo dos Resultados
resultados = Label(janela, text='')
resultados.grid(column=1, row=4)

botao = Button(janela, text='Fechar', command=fechar_janela)
botao.grid(column=1, row=5)

janela.mainloop()

















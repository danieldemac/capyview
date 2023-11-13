# Contribuição para o Projeto Capyview - Automatização Simplificada

## Diretrizes para Contribuição

O projeto Capyview recebe com prazer contribuições da comunidade. Antes de enviar suas contribuições, por favor, leia as seguintes diretrizes.

### Fluxo de Trabalho de Contribuição

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações: `git checkout -b nome-da-sua-branch`.
3. Faça suas alterações e comite: `git commit -am 'Descrição concisa das alterações'`.
4. Push para a sua branch: `git push origin nome-da-sua-branch`.
5. Envie um pull request.

### Estilo de Código

Mantenha um estilo de código consistente com o projeto. Utilize as convenções de codificação estabelecidas.

### Relatório de Problemas

Ao relatar problemas, forneça informações detalhadas sobre o problema e, se possível, inclua passos para reprodução.

### Adição de Funcionalidades

Se estiver adicionando uma nova funcionalidade, forneça uma descrição clara e adicione documentação conforme necessário.

### Correção de Bugs

Para correções de bugs, descreva o problema e como ele foi corrigido.

### Documentação

Atualize a documentação conforme necessário para refletir as alterações realizadas.

### Testes

Certifique-se de que suas alterações foram testadas de forma adequada e não introduziram novos problemas.

### Estrutura do Projeto

O projeto está organizado com os seguintes diretórios:

- `__pycache__`: Armazena arquivos de cache do Python.
- `images`: Contém a logo do Capyview.
- `implementacao_testes`: Testes de novas funcionalidades.
- `modelos`: Modelos usados como base para criação de views e rotas.
- `resultado`: Resultados das automações.
- `LICENSE`: Licença Apache 2.0.
- `README.md`: Este documento.
- `funcao_html.py`: Função para criação do HTML.
- `funcao_js.py`: Função para criação do JavaScript.
- `funcao_model.py`: Função para criação do model.
- `funcao_rota.py`: Função para criação da rota.
- `funcoes_repositorio.py`: Repositório de todas as funções.
- `main.py`: Arquivo principal do programa.

### Como Usar

Atualmente, o programa funciona apenas no terminal através do arquivo `main.py`. Escreva o comando para a criação de tabelas dentro de um arquivo chamado `modelos/tabela.php`. Exemplo de comando:

```sql
CREATE TABLE tabela_testes
(
    id bigint,
    name character varying(200),
    relationship character varying(50),
    birth date,
    created_at timestamp,
    status "char",
    updated_at timestamp,
    deleted_at timestamp
)

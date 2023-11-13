<h1 align="center">Automatização Simplificada: Capyview - Uma Ferramenta para Geração de HTML, Interfaces e Rotas em Projetos PHP/Laravel</h1> 
<p align="center">
  <img width="300" height="300" src="images/capyview.png" alt="Logo do Capyview">
</p>
Capyview é uma ferramenta para a automatização da geração de HTML, interfaces e caminhos em projetos PHP/Laravel.

[![GitHub](https://img.shields.io/badge/Licença-Apache%202.0-blue)](https://github.com/danieldemac/capyview/blob/main/LICENSE)

## Visão Geral

No mundo do desenvolvimento de projetos PHP/Laravel, a criação de múltiplas páginas, interfaces de usuário e configurações de rotas pode ser uma tarefa demorada e propensa a erros. É nesse cenário desafiador que o “Capyview” surge como uma solução para melhorar a celeridade dos projetos Web. Esta ferramenta é projetada para simplificar e automatizar o processo de desenvolvimento, economizando tempo e esforço na geração de código HTML, criação de interfaces de usuário e configurações de rotas.

Com o **Capyview**, você pode:

- Gerar páginas HTML facilmente a partir de modelos predefinidos.
- Criar interfaces de usuário de maneira eficiente.
- Definir rotas no Laravel de forma automática.

  ## Estrutura do Projeto

Este repositório está organizado da seguinte forma:

- `.github/ISSUE_TEMPLATE`: Diretório que contém modelos de issues.
- `__pycache__`: Diretório utilizado pelo Python para armazenar arquivos de cache contendo versões compiladas (bytecode) de módulos Python, visando melhorar o desempenho de importação.
- `images`: Pasta que contém a logo do Capyview.
- `implementação_testes`: Pasta que inclui testes de novas funcionalidades.
- `modelos`: Pasta que contém modelos usados como base para a criação de views e rotas.
- `resultado`: Pasta que contém os resultados das automações.
- `CODE_OF_CONDUCT.md`: Arquivo que foi para refletir as diretrizes de conduta para contribuição no projeto.
- `CONTRIBUTING.md`: Arquivo que contém informações sobre como contribuir para o projeto.
- `LICENSE`: [Licença Apache 2.0](https://github.com/danieldemac/capyview/blob/main/LICENSE).
- `README.md`: Documento que você está lendo agora, contendo informações sobre o projeto.
- `SECURITY.md`: Arquivo que contem informações sobre políticas de segurança.
- `funcao_html.py`: Arquivo que contém a função para a criação do HTML.
- `funcao_js.py`: Arquivo que contém a função para a criação do JavaScript.
- `funcao_model.py`: Arquivo que contém a função para a criação do model.
- `funcao_rota.py`: Arquivo que contém a função para a criação da rota.
- `funcoes_repositorio.py`: Arquivo que serve como repositório para todas as funções.
- `main.py`: Arquivo principal do programa.

## Como Usar

No momento o programa funciona apenas no terminal pelo Arquivo `main.py`. Você deve escreve o comando para criação de tabelas dentro de um arquivo chamado `modelos/tabela.php`.
Exemplo de comando:
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
```
Ao rodar o programa ele vai criar uma base para views, rotas e controllers usando essa tabela como base. Mais funcionalidades e modelos estão sendo elaborados para esse projeto.


## Licença

Este projeto é distribuído sob a [Licença Apache 2.0](https://github.com/danieldemac/capyview/blob/main/LICENSE). Leia o arquivo de licença para obter mais informações.

---

<h2 align="center">Capyview é desenvolvido por <a href='https://github.com/danieldemac'>Daniel Cabral</a>.</h2>

## Instalação

1. Crie um clone repository na sua máquina local:

```bash
git clone https://github.com/danieldemac/capyview.git

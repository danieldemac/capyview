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

- `__pycache__`: é um diretório usado pelo Python para armazenar arquivos de cache que contêm versões compiladas (bytecode) de módulos Python para melhorar o desempenho de importação.
- `images`: Pasta com a logo do Capyview.
- `implementação_testes`: Pasta com testes de novas funcionalidades.
- `modelos`: Pasta com os modelos usados como base para criação das views e rotas.
- `resultado`: Pasta com os resultados das automações.
- `LICENSE`: [Licença Apache 2.0](https://github.com/danieldemac/capyview/blob/main/LICENSE).
- `README.md`: O que você está lendo!
- `funcao_html.py`: Função para criação do html.
- `funcao_js.py`: Função para criação do JavaScript.
- `funcao_model.py`: Função para criação do model.
- `funcao_rota.py`: Função para criação da rota.
- `funcoes_repositorio.py`: Repositório de todas as funções.
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

**Capyview** é desenvolvido por [Daniel Cabral]. [GitHub do Projeto](https://github.com/danieldemac/capyview)

## Installation.

1. Clone this repository to your local machine:

```bash
git clone https://github.com/danieldemac/capyview.git

<h1 align="center">Automatização Simplificada: Capyview - Uma Ferramenta para Geração de HTML, Interfaces e Rotas em Projetos PHP/Laravel.</h1>  
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

## Como Usar

No momento o programa funciona no terminal pelo Arquivo `main.py` na pasta base_capyview ou no arquivo `main.py` na pasta tkinter_capyview. No primeiro caso vocÊ deve escreve o comando para criação de tabelas dentro de um arquivo chamado `modelos/tabela.php`.
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

O segundo arquivo `main.py` (na pasta tkinter_capyview) possui uma interface gráfica na qual você pode colocar o mesmo comando de criação de tabela para criar os arquivos.

## Site do Projeto disponivel pelo Netlify!

Link disponivel neste endereço: https://capyview.netlify.app/

## Licença

Este projeto é distribuído sob a [Licença Apache 2.0](https://github.com/danieldemac/capyview/blob/main/LICENSE). Leia o arquivo de licença para obter mais informações.

---

<h2 align="center">Capyview é desenvolvido por <a href='https://github.com/danieldemac'>Daniel Cabral</a>.</h2>

## Instalação

1. Crie um clone repository na sua máquina local:

```bash
git clone https://github.com/danieldemac/capyview.git

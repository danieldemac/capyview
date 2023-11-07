import os

def gerar_php_teste(singular, plural):
    file_name = r"C:\xampp\htdocs\capyview\capyview\public\index.php"
    template = f"""
@extends('voyager::master')
@section('page_title', 'Portal DTM - {plural}')

@section('page_header')
    <h1 class="page-title"><i class="icon voyager-receipt"></i>{plural}</h1>
    <button class="btn btn-success btn-sm" type="button" data-toggle="modal" data-target="#modal-create-{singular}" id="bt-create-{singular}">
        <i class="voyager-plus"></i> Adicionar
    </button>
    <button class="btn btn-danger btn-sm" type="button" data-toggle"modal" data-target="#model-delete-{plural}" id="bt-delete-{plural}" disabled="true">
        <i class="voyager-trash"></i> Exclusão em massa
    </button>
@stop

@section('content')

<div class="panel panel-bordered">
    <div class="panel-body">
        <div class="row justify-content-center">
            <div class="card">
                <div class="card-body">
                    <div class="card-title"></div>
                    <table id="dt-{plural}" class="table table-bordered table-hover">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Clinica</th>
                                <th>Médico</th>
                                <th>Cid</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="modal-create-{singular}" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <section id="loading-create-{singular}"><div id="loading-content-create-{singular}"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Adicionar {singular}</h4><hr></div>
            <div class="modal-body">
                <div class="alert alert-danger"  role="alert" style="display: none;"></div>
                <div class="alert alert-success" role="alert" style="display: none;"></div>
 
                <form id="form-create-{singular}" enctype="multipart/form-data">
                    <div class="form-row">
                        <div class="form-group mb-3">
                            <input type="hidden" class="form-control" id="id-{singular}" value="">
                            <label class="form-label" for="clinic-name">Nome da Clinica*</label>
                            <input type="text" class="form-control required" id="clinic-name">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class "form-label" for="clinic-phone">Telefone da Clinica*</label>
                            <input type="text" class="form-control required" id="clinic-phone">
                        </div>
                    </div>
    
                    <div class "form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="medical-record">Registo Médico</label>
                            <input type="text" class="form-control required" id="medical-record">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label for="gender" for="cid" form-label">CID</label><br>
                            <select class="form-control required" id="cid" name="cid">
                                <option value="0">A00 - Cólera</option>
                                <option value="1">A00.0 - Cólera Devida a Vibrio Cholerae 01, Biótipo Cholerae</option>
                                <option value="2">A00.1 - Cólera Devida a Vibrio Cholerae 01, Biótipo El Tor</option>
                                <option value="3">A00.9 - Cólera Não Especificada</option>
                                <option value="4">A01 - Febres Tifóide e Paratifóide</option>
                                <option value="5">A01.0 - Febre Tifóide</option>
                                <option value="5">A01.1 - Febre Paratifóide A</option>
                                <option value="7">A01.2 - Febre Paratifóide B</option>
                                <option value="8">A01.3 - Febre Paratifóide C</option>
                                <option value="9">A01.4 - Febre Paratifóide Não Especificada</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="days-away">Dias Afastados</label>
                            <input type="text" class="form-control required" id="days-away">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for "{singular}-data">Data do {singular}</label>
                            <input type="text" class="form-control required" id "{singular}-data">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for "{singular}-companion">Companhante</label><br>
                            <input type="checkbox" data-toggle="toggle" data-on="Sim" data-off="Não" class="toggle" id "{singular}-companion" checked>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for "file">Arquivo</label><br>
                            <input type="file" name="file" id="file" class="form-control"/>
                        </div>
                    </div>
                </form>
            </div>

            <div class="modal-footer">
                <hr>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Fechar</button>
                <button type="button" class="btn btn-success" id="submit-update-create-{singular}">Salvar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-{singular}">
    <div class="modal-dialog">
        <section id="loading-delete-id"><div id="loading-content-delete-id"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir {singular}</h4><hr></div>
            <div class "modal-body"><p>Deseja <b>EXCLUIR</b> o {singular} ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-success" id="submit-delete-{singular}">Sim</button>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-{plural}">
    <div class="modal-dialog">
        <section id="loading-delete-ids"><div id="loading-content-delete-ids"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir {plural}</h4><hr></div>
            <div class="modal-body"><p>Tem certeza que deseja <b>EXCLUIR</b> a(s) {plural} ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" id="submit-delete-{plural}">Sim</button>
                <button type="button" class="btn btn-default" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-view-file">
    <div class="modal-dialog">
        <div class="modal-content" >
            <div class="modal-header"><h4 class="modal-title">Visualizar Arquivo</h4><hr></div>
            <div class="modal-body"><div id "{singular}-view-file"></div></div>
            <div class="modal-footer"><button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button></div>
        </div>
    </div>
</div>
"""

    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(template)
    return file_name

# Exemplo de uso:
SINGULAR = input("Digite o valor de SINGULAR: ")
PLURAL = input("Digite o valor de PLURAL: ")
file_name = gerar_php_teste(SINGULAR, PLURAL)
print(f"Arquivo '{file_name}' foi criado com sucesso.")
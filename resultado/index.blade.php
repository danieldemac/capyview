@extends('voyager::master')
@section('page_title', 'Página criada - user_dependent')

@section('page_header')
    <h1 class="page-title"><i class="icon voyager-receipt"></i>Nome</h1>
    <button class="btn btn-success btn-sm" type="button" data-toggle="modal" data-target="#modal-create-user_dependent" id="bt-create-user_dependent">
        <i class="voyager-plus"></i> Adicionar
    </button>
    <button class="btn btn-danger btn-sm" type="button" data-toggle="modal" data-target="#model-delete-user_dependents" id="bt-delete-user_dependents" disabled="true">
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
                    <table id="dt-user_dependents" class="table table-bordered table-hover">
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

<div class="modal fade" id="modal-create-user_dependent" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <section id="loading-create-user_dependent"><div id="loading-content-create-user_dependent"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Adicionar Atestados</h4><hr></div>
            <div class="modal-body">
                <div class="alert alert-danger"  role="alert" style="display: none;"></div>
                <div class="alert alert-success" role="alert" style="display: none;"></div>
 
                <form id="form-create-user_dependent" enctype="multipart/form-data">
                    <div class="form-row">
                        <div class="form-group mb-3">
                            <input type="hidden" class="form-control" id="id-user_dependent" value="">
                            <label class="form-label" for="clinic-name">Nome da Clinica*</label>
                            <input type="text" class="form-control required" id="clinic-name">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="clinic-phone">Telefone da Clinica*</label>
                            <input type="text" class="form-control required" id="clinic-phone">
                        </div>
                    </div>
    
                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="medical-record">Registo Médico</label>
                            <input type="text" class="form-control required" id="medical-record">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label for="gender" for="cid" form-label>CID</label><br>
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
                            <label class="form-label" for="user_dependent-data">Data do Atestado</label>
                            <input type="text" class="form-control required" id="user_dependent-data">
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="user_dependent-companion">Companhante</label><br>
                            <input type="checkbox" data-toggle="toggle" data-on="Sim" data-off="Não" class="toggle" id="user_dependent-companion" checked>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group mb-3">
                            <label class="form-label" for="file">Arquivo</label><br>
                            <input type="file" name="file" id="file" class="form-control"/>
                        </div>
                    </div>
                </form>
            </div>

            <div class="modal-footer">
                <hr>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Fechar</button>
                <button type="button" class="btn btn-success" id="submit-update-create-user_dependent">Salvar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-user_dependent">
    <div class="modal-dialog">
        <section id="loading-delete-id"><div id="loading-content-delete-id"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir Atestado</h4><hr></div>
            <div class="modal-body"><p>Deseja <b>EXCLUIR</b> o atestado ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-success" id="submit-delete-user_dependent">Sim</button>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-user_dependents">
    <div class="modal-dialog">
        <section id="loading-delete-ids"><div id="loading-content-delete-ids"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir Atestado</h4><hr></div>
            <div class="modal-body"><p>Tem certeza que deseja <b>EXCLUIR</b> a(s) Atestado(s) ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" id="submit-delete-user_dependents">Sim</button>
                <button type="button" class="btn btn-default" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-view-file">
    <div class="modal-dialog">
        <div class="modal-content" >
            <div class="modal-header"><h4 class="modal-title">Visualizar Arquivo</h4><hr></div>
            <div class="modal-body"><div id="user_dependent-view-file"></div></div>
            <div class="modal-footer"><button type="button" class="btn btn-default" data-dismiss="modal">Fechar</button></div>
        </div>
    </div>
</div>


@endsection

@section('css')
    <style>
        .dt-buttons { float: right; margin: 0 0 0 25%; }
        
        .loading { z-index: 20; position: absolute; top: 0; left:-5px; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.4); }
        .loading-content { position: absolute; border: 16px solid #f3f3f3; border-top: 16px solid #3498db; border-radius: 50%; width: 50px; height: 50px; top: 40%; left: 35%; animation: spin 2s linear infinite; }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
    <link rel="stylesheet" href="{{ asset('css/data-tables/jquery.dataTables.min.css') }}">
    <link rel="stylesheet" href="{{ asset('css/data-tables/buttons.dataTables.min.css') }}">
@stop

@section('javascript')
    <script type="text/javascript" src="{{ asset('js/data-tables/jquery.dataTables.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset('js/data-tables/dataTables.buttons.min.js') }}"></script>

    <script type="text/javascript" src="{{ asset('js/data-tables/buttons.html5.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset('js/data-tables/buttons.print.min.js') }}"></script>

    <script type="text/javascript" src="{{ asset('js/data-tables/jszip.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset('js/data-tables/pdfmake.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset('js/data-tables/vfs_fonts.js') }}"></script>
    
    <script src="{{ asset('js/user_dependents.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.min.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.pt.min.js') }}" type="text/javascript"></script>

    <script>
        $("#user_dependent-data").datepicker({
            daysOfWeekDisabled: [0, 7],
            todayHighlight: false,
            language: 'pt-BR',
            format: 'dd/mm/yyyy'
        })
    </script>

@stop


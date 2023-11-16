@extends('voyager::master')
@section('page_title', 'Página criada - tabela_example')

@section('page_header')
    <h1 class="page-title"><i class="icon voyager-receipt"></i>Nome</h1>
    <button class="btn btn-success btn-sm" type="button" data-toggle="modal" data-target="#modal-create-tabela_example" id="bt-create-tabela_example">
        <i class="voyager-plus"></i> Adicionar
    </button>
    <button class="btn btn-danger btn-sm" type="button" data-toggle="modal" data-target="#model-delete-tabela_examples" id="bt-delete-tabela_examples" disabled="true">
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
                    <table id="dt-tabela_examples" class="table table-bordered table-hover">
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

<div class="modal fade" id="modal-create-tabela_example" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <section id="loading-create-tabela_example"><div id="loading-content-create-tabela_example"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Adicionar Atestados</h4><hr></div>
            <div class="modal-body">
                <div class="alert alert-danger"  role="alert" style="display: none;"></div>
                <div class="alert alert-success" role="alert" style="display: none;"></div>
 
                <form id="form-create-tabela_example" enctype="multipart/form-data">

                <!-- // ESTRUTURA DE REPETIÇÃO -->
                    <div class="form-row">
                        <div class="form-group mb-3">
                            <input type="hidden" class="form-control" id="id-tabela_example" value="">
                            <label class="form-label" for="clinic-name">Idade Filho*</label>
                            <input type="text" class="form-control required" id="idade-filho">
                        </div>
                    </div>
                <!-- // ESTRUTURA DE REPETIÇÃO -->

                </form>
            </div>

            <div class="modal-footer">
                <hr>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Fechar</button>
                <button type="button" class="btn btn-success" id="submit-update-create-tabela_example">Salvar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-tabela_example">
    <div class="modal-dialog">
        <section id="loading-delete-id"><div id="loading-content-delete-id"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir Atestado</h4><hr></div>
            <div class="modal-body"><p>Deseja <b>EXCLUIR</b> o atestado ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-success" id="submit-delete-tabela_example">Sim</button>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-tabela_examples">
    <div class="modal-dialog">
        <section id="loading-delete-ids"><div id="loading-content-delete-ids"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir Atestado</h4><hr></div>
            <div class="modal-body"><p>Tem certeza que deseja <b>EXCLUIR</b> a(s) Atestado(s) ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" id="submit-delete-tabela_examples">Sim</button>
                <button type="button" class="btn btn-default" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-view-file">
    <div class="modal-dialog">
        <div class="modal-content" >
            <div class="modal-header"><h4 class="modal-title">Visualizar Arquivo</h4><hr></div>
            <div class="modal-body"><div id="tabela_example-view-file"></div></div>
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
    
    <script src="{{ asset('js/tabela_examples.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.min.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.pt.min.js') }}" type="text/javascript"></script>

    <script>
        $("#tabela_example-data").datepicker({
            daysOfWeekDisabled: [0, 7],
            todayHighlight: false,
            language: 'pt-BR',
            format: 'dd/mm/yyyy'
        })
    </script>

@stop


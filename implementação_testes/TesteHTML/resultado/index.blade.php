@extends('voyager::master')
@section('page_title', 'Página criada - teste')

@section('page_header')
    <h1 class="page-title"><i class="icon voyager-receipt"></i>Nome teste</h1>
    <button class="btn btn-success btn-sm" type="button" data-toggle="modal" data-target="#modal-create-teste" id="bt-create-teste">
        <i class="voyager-plus"></i> Adicionar
    </button>
    <button class="btn btn-danger btn-sm" type="button" data-toggle="modal" data-target="#model-delete-testes" id="bt-delete-testes" disabled="true">
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
                    <table id="dt-testes" class="table table-bordered table-hover">
                        <thead>
						<tr>
							<th>Name</th>
							<th>Relationship</th>
							<th>Status</th>
							<th>Idade_filho</th>
							<th>Bora</th>
							<th>Bill</th>
							<th>Lol</th>
							<th>Final</th>
						</tr>
                        </thead>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="modal-create-teste" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <section id="loading-create-teste"><div id="loading-content-create-teste"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Adicionar testes</h4><hr></div>
            <div class="modal-body">
                <div class="alert alert-danger"  role="alert" style="display: none;"></div>
                <div class="alert alert-success" role="alert" style="display: none;"></div>
 
                <form id="form-create-teste" enctype="multipart/form-data"><form id="form-create-teste" enctype="multipart/form-data">
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="name">Name*</label>
					<input type="text" class="form-control required" id="name">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="relationship">Relationship*</label>
					<input type="text" class="form-control required" id="relationship">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="status">Status*</label>
					<input type="text" class="form-control required" id="status">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="idade_filho">Idade filho</label>
					<input type="text" class="form-control " id="idade_filho">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="Bora">Bora*</label>
					<input type="text" class="form-control required" id="Bora">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="Bill">Bill*</label>
					<input type="text" class="form-control required" id="Bill">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="LOL">Lol*</label>
					<input type="text" class="form-control required" id="LOL">
				</div>
			</div>
			<div class="form-row">
				<div class="form-group mb-3">
					<label class="form-label" for="Final">Final*</label>
					<input type="text" class="form-control required" id="Final">
				</div>
			</div>
</form></form>
            </div>

            <div class="modal-footer">
                <hr>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Fechar</button>
                <button type="button" class="btn btn-success" id="submit-update-create-teste">Salvar</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-teste">
    <div class="modal-dialog">
        <section id="loading-delete-id"><div id="loading-content-delete-id"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir teste</h4><hr></div>
            <div class="modal-body"><p>Deseja <b>EXCLUIR</b> o teste ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-success" id="submit-delete-teste">Sim</button>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-delete-testes">
    <div class="modal-dialog">
        <section id="loading-delete-ids"><div id="loading-content-delete-ids"></div></section>
        <div class="modal-content">
            <div class="modal-header"><h4 class="modal-title">Excluir teste</h4><hr></div>
            <div class="modal-body"><p>Tem certeza que deseja <b>EXCLUIR</b> a(s) teste(s) ?</p></div>
            <div class="modal-footer">
                <button type="button" class="btn btn-danger" id="submit-delete-testes">Sim</button>
                <button type="button" class="btn btn-default" data-dismiss="modal">Não</button>
            </div>
        </div>
    </div>
</div>

<div class="modal" id="model-view-file">
    <div class="modal-dialog">
        <div class="modal-content" >
            <div class="modal-header"><h4 class="modal-title">Visualizar Arquivo</h4><hr></div>
            <div class="modal-body"><div id="teste-view-file"></div></div>
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
    
    <script src="{{ asset('js/testes.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.min.js') }}" type="text/javascript"></script>
    <script src="{{ asset('js/bootstrap-datepicker.pt.min.js') }}" type="text/javascript"></script>

    <script>
        $("#teste-data").datepicker({
            daysOfWeekDisabled: [0, 7],
            todayHighlight: false,
            language: 'pt-BR',
            format: 'dd/mm/yyyy'
        })
    </script>

@stop
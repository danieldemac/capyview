function showLoading(a, b) {
    document.querySelector(a).classList.add('loading');
    document.querySelector(b).classList.add('loading-content');
}

function hideLoading(a, b) {
    document.querySelector(a).classList.remove('loading');
    document.querySelector(b).classList.remove('loading-content');
}

function formClear() {
	$('#id-tabela_rafael').val('');
	$('#name').val('');
	$('#relationship').val('');
	$('#status').val('');
	$('#idade_filho').val('');
    $('#tabela_rafael-data').val('');
    $('#tabela_rafael-companion').val('');
}

$(window).on('load', function(){
$('#cid').select2();
var inputSearch;
var timeout = null;
var blockKeyCodes = [16, 17, 18, 20, 27, 32, 33, 34, 37, 38, 39, 40, 91, 92, 93, 144];

var table = $('#dt-{tabela_rafaels}').DataTable({
    processing: true,
    serverSide: true,
    autoWidth: false,
    pageLength: 5,
    searchDelay: 1000,
    order: [[ 1, "desc" ]],
    lengthMenu: [5, 10, 25, 50],
    columnDefs: [{ "targets": 0, "orderable": false },{ "targets": 4, "orderable": false }],
    ajax: { url:"get-{tabela_rafaels}" },
    columns: [ 
        { data: 'checkbox', sClass: 'text-center', serachable: false },
		{ data: 'name' },
		{ data: 'relationship' },
		{ data: 'status' },
		{ data: 'idade_filho' },
        { data: 'action', serachable: false  }
],
language: {url:"/js/data-tables/pt_br.json"},
dom: 'lBfrtip',
buttons: {
    buttons: [
        { id: 'excel', extend: 'excel', titleAttr: "Export to excel", text: '<b>Excel</b>', className: '' ,"action": exportaction },
        { id: 'pdf', extend: 'pdf', titleAttr: "Export to pdf", text: "<b>PDF</b>","action": exportaction },
    ]
},
initComplete: function () {
    $('.dataTables_filter input').unbind();
    $('.dataTables_filter input').keyup('input', function (e) {
        if (e.keyCode !== 17)
            if ((this.value.length > 2 || this.value.length == 0) && jQuery.inArray(e.keyCode, blockKeyCodes) == -1) {
                inputSearch = this.value;
                clearTimeout(timeout);
                timeout = setTimeout(function () {
                    table.search(inputSearch).draw();
                },
                table.context[0].searchDelay);
            }
    });
},
});

function exportaction(e, dt, button, config) {
$(".btn").prop('disabled', true);
button 	 = button[0].className;
var self = this;

dt.one('preXhr', function (e, settings, data) {
    data.start = 0;
    data.length = dt.settings()[0]._iRecordsDisplay;
    dt.one('preDraw', function (e, settings) {
        if (button.indexOf('buttons-excel') >= 0) {
            $.fn.dataTable.ext.buttons.excelHtml5.action.call(self, e, dt, button, config);
        }  else if (button.indexOf('buttons-pdf') >= 0) {
            $.fn.dataTable.ext.buttons.pdfHtml5.action.call(self, e, dt, button, config) 
        }
        $(".btn").prop('disabled', false)
        return false;
    });
});
dt.ajax.reload();
}
});


$(document).ready(function(){

var tabela_rafaels_selects = [];
var tabela_rafael_id;

$('body').on('click', '.tabela_rafael_checkbox', function (e) {
var arrayChecked = []
var checkboxesMarcados = $("input[type='checkbox']:checked");
checkboxesMarcados.each(function () { arrayChecked.push($(this).val());});

tabela_rafaels_selects = arrayChecked;
tabela_rafaels_selects.length > 0 ? $('#bt-delete-tabela_rafaels').removeAttr('disabled') : $('#bt-delete-tabela_rafaels').attr('disabled', 'disabled');
})

$('body').on('click', '#bt-view-file', function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/tabela_rafaels-view-file/" + $(this).data('id'),
    method: 'GET',
    data: { id: $(this).data('id') },
    success: function (result) {
        $('#tabela_rafael-view-file').html(result.html);
    },
    error: function(result){
        console.log('ERRO');
    }
});
});

$('body').on('click', '#bt-delete-tabela_rafael', function () { tabela_rafael_id = $(this).data('id') })
$('#submit-delete-tabela_rafael').click(function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/tabela_rafaels",
    method: 'DELETE',
    data:{ids: JSON.stringify(tabela_rafael_id)},
    headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') },
    success: function (result) {
        console.log(result);
        $('#dt-tabela_rafaels').DataTable().ajax.reload();
        $('.alert-success').hide();
        //$('#deletarFeriado').modal('hide');
        window.location = document.URL;
    },
    error: function(result){
        $('.alert-danger').show();
           $('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
        hideLoading('#loading-create-tabela_rafael', '#loading-content-create-tabela_rafael');
    }
});
});

$('body').on('click', '#bt-edit', function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/tabela_rafaels/" + $(this).data('id'),
    method: 'GET',
    success: function (result) {
        $('#id-tabela_rafael').val(1);
		$('#name').val();
		$('#relationship').val();
		$('#status').val();
		$('#idade_filho').val();
		$('#tabela_rafael-data').val();
		$('#tabela_rafael-companion').val();
		$('.modal-title').html('Editar Atestado');
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

	$('body').on('click', '#bt-create-tabela_rafael', function (e) {
        e.preventDefault();
		formClear();
		$('.modal-title').html('Adicionar Atestado');
    });






    $('#submit-delete-tabela_rafaels').click(function (e) {
		alert($(this).data('id'));
		alert(tabela_rafaels_selects);

        e.preventDefault();
        $.ajax({
            url: "/admin/tabela_rafaels",
            data:{ids: JSON.stringify(tabela_rafaels_selects)},
            method: 'DELETE',
			headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')},
            success: function (result) {
				console.log(result);
                $('#dt-tabela_rafaels').DataTable().ajax.reload();
                $('.alert-success').hide();
                $('#model-delete-tabela_rafaels').modal('hide');
                 window.location = document.URL;
            },
			error: function(result){
				console.log(result);
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-tabela_rafael', '#loading-content-create-tabela_rafael');
			}
        });
    });

	$('#submit-update-create-tabela_rafael').click(function (e) {
		$('.alert-danger').hide();
        $('.alert-success').hide();

        e.preventDefault();
        showLoading('#loading-create-tabela_rafael', '#loading-content-create-tabela_rafael');

		var file 	  = $('#file').prop('files')[0];
		var form_data = new FormData();
		var dateParts = $('#tabela_rafael-data').val().split('/');
	
		// ESTRUTURA DE REPETIÇÃO
		form_data.append('id_tabela_rafael', $('#id-tabela_rafael').val());
		// 

        $.ajax({
            url: "/admin/tabela_rafaels",
            method: 'POST',
			data: form_data,
			contentType : false,
    		processData : false,
			headers: {'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')},

            success: function (result) {
				console.log(result);
                $('.alert-danger').hide();
                $('.alert-success').show();
				$('.alert-success').append('<strong>Sucesso! </strong>&nbsp; ' + result.success + '');
                $('#dt-tabela_rafaels').DataTable().ajax.reload();
                window.location = document.URL;
            },
			error: function(result){
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-tabela_rafael', '#loading-content-create-tabela_rafael');
			}
        });
    });


	$('#submit-edit-tabela_rafael').click(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/tabela_rafaels/" + $(this).data('id'),
            method: 'GET',
            data: { id: $(this).data('id') },
            success: function (result) {
                $('#tabela_rafael-view-file').html(result.html);
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

});
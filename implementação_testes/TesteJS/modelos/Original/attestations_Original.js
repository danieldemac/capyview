function showLoading(a, b) {
    document.querySelector(a).classList.add('loading');
    document.querySelector(b).classList.add('loading-content');
}

function hideLoading(a, b) {
    document.querySelector(a).classList.remove('loading');
    document.querySelector(b).classList.remove('loading-content');
}

function formClear() {
	$('#file').val('');
	$('#id-attestation').val('');
	$('#clinic-name').val('');
	$('#clinic-phone').val('');
	$('#medical-record').val('');
	$('#cid').val('');
	$('#days-away').val('');
	$('#attestation-data').val('');
	$('#attestation-companion').val('');
}

$(window).on('load', function(){
	$('#cid').select2();
	var inputSearch;
	var timeout = null;
	var blockKeyCodes = [16, 17, 18, 20, 27, 32, 33, 34, 37, 38, 39, 40, 91, 92, 93, 144];

	var table = $('#dt-attestations').DataTable({
		processing: true,
		serverSide: true,
		autoWidth: false,
		pageLength: 5,
		searchDelay: 1000,
		order: [[ 1, "desc" ]],
		lengthMenu: [5, 10, 25, 50],
		columnDefs: [{ "targets": 0, "orderable": false },{ "targets": 4, "orderable": false }],
		ajax: { url:"get-attestations" },
		columns: [ 
			{ data: 'checkbox', sClass: 'text-center', serachable: false },
			{ data: 'clinic_name' }, 
			{ data: 'medical_record' }, 
			{ data: 'cid' }, 
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

	var attestations_selects = [];
	var attestation_id;

	$('body').on('click', '.attestation_checkbox', function (e) {
        var arrayChecked = []
        var checkboxesMarcados = $("input[type='checkbox']:checked");
        checkboxesMarcados.each(function () { arrayChecked.push($(this).val());});

        attestations_selects = arrayChecked;
        attestations_selects.length > 0 ? $('#bt-delete-attestations').removeAttr('disabled') : $('#bt-delete-attestations').attr('disabled', 'disabled');
    })

	$('body').on('click', '#bt-view-file', function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/attestations-view-file/" + $(this).data('id'),
            method: 'GET',
            data: { id: $(this).data('id') },
            success: function (result) {
                $('#attestation-view-file').html(result.html);
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

	$('body').on('click', '#bt-delete-attestation', function () { attestation_id = $(this).data('id') })
    $('#submit-delete-attestation').click(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/attestations",
            method: 'DELETE',
			data:{ids: JSON.stringify(attestation_id)},
			headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') },
            success: function (result) {
				console.log(result);
                $('#dt-attestations').DataTable().ajax.reload();
                $('.alert-success').hide();
                //$('#deletarFeriado').modal('hide');
                window.location = document.URL;
            },
			error: function(result){
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-attestation', '#loading-content-create-attestation');
			}
        });
    });

	$('body').on('click', '#bt-edit', function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/attestations/" + $(this).data('id'),
            method: 'GET',
            success: function (result) {
				$('#id-attestation').val(1);
				$('#clinic-name').val('joao');
				$('#clinic-phone').val('bbbbbbbbb');
				$('#medical-record').val('asdasd');
				$('#cid').val();
				$('#days-away').val();
				$('#attestation-data').val();
				$('#attestation-companion').val();
				$('.modal-title').html('Editar Atestado');
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

	$('body').on('click', '#bt-create-attestation', function (e) {
        e.preventDefault();
		formClear();
		$('.modal-title').html('Adicionar Atestado');
    });






    $('#submit-delete-attestations').click(function (e) {
		alert($(this).data('id'));
		alert(attestations_selects);

        e.preventDefault();
        $.ajax({
            url: "/admin/attestations",
            data:{ids: JSON.stringify(attestations_selects)},
            method: 'DELETE',
			headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')},
            success: function (result) {
				console.log(result);
                $('#dt-attestations').DataTable().ajax.reload();
                $('.alert-success').hide();
                $('#model-delete-attestations').modal('hide');
                 window.location = document.URL;
            },
			error: function(result){
				console.log(result);
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-attestation', '#loading-content-create-attestation');
			}
        });
    });

	$('#submit-update-create-attestation').click(function (e) {
		$('.alert-danger').hide();
        $('.alert-success').hide();

        e.preventDefault();
        showLoading('#loading-create-attestation', '#loading-content-create-attestation');

		var file 	  = $('#file').prop('files')[0];
		var form_data = new FormData();
		var dateParts = $('#attestation-data').val().split('/');
	
		form_data.append('id_attestation', $('#id-attestation').val());
		form_data.append('clinic_name', $('#clinic-name').val());
		form_data.append('clinic_phone', $('#clinic-phone').val());
		form_data.append('medical_record', $('#medical-record').val());
		form_data.append('cid', $('#cid').val());
		form_data.append('days_away', $('#days-away').val());
		form_data.append('attestation_data', dateParts[2] + '-' + dateParts[1] + '-' + dateParts[0]);
		form_data.append('attestation_companion', $('#attestation-companion').val());
		form_data.append('file', file);

        $.ajax({
            url: "/admin/attestations",
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
                $('#dt-attestations').DataTable().ajax.reload();
                window.location = document.URL;
            },
			error: function(result){
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-attestation', '#loading-content-create-attestation');
			}
        });
    });


	$('#submit-edit-attestation').click(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/attestations/" + $(this).data('id'),
            method: 'GET',
            data: { id: $(this).data('id') },
            success: function (result) {
                $('#attestation-view-file').html(result.html);
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

});

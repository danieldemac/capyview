		$('#{singular}-data').val();
		$('#{singular}-companion').val();
		$('.modal-title').html('Editar Atestado');
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

	$('body').on('click', '#bt-create-{singular}', function (e) {
        e.preventDefault();
		formClear();
		$('.modal-title').html('Adicionar Atestado');
    });






    $('#submit-delete-{plural}').click(function (e) {
		alert($(this).data('id'));
		alert({plural}_selects);

        e.preventDefault();
        $.ajax({
            url: "/admin/{plural}",
            data:{ids: JSON.stringify({plural}_selects)},
            method: 'DELETE',
			headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')},
            success: function (result) {
				console.log(result);
                $('#dt-{plural}').DataTable().ajax.reload();
                $('.alert-success').hide();
                $('#model-delete-{plural}').modal('hide');
                 window.location = document.URL;
            },
			error: function(result){
				console.log(result);
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-{singular}', '#loading-content-create-{singular}');
			}
        });
    });

	$('#submit-update-create-{singular}').click(function (e) {
		$('.alert-danger').hide();
        $('.alert-success').hide();

        e.preventDefault();
        showLoading('#loading-create-{singular}', '#loading-content-create-{singular}');

		var file 	  = $('#file').prop('files')[0];
		var form_data = new FormData();
		var dateParts = $('#{singular}-data').val().split('/');
	
		// ESTRUTURA DE REPETIÇÃO
		form_data.append('id_{singular}', $('#id-{singular}').val());
		// 

        $.ajax({
            url: "/admin/{plural}",
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
                $('#dt-{plural}').DataTable().ajax.reload();
                window.location = document.URL;
            },
			error: function(result){
                $('.alert-danger').show();
               	$('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
                hideLoading('#loading-create-{singular}', '#loading-content-create-{singular}');
			}
        });
    });


	$('#submit-edit-{singular}').click(function (e) {
        e.preventDefault();
        $.ajax({
            url: "/admin/{plural}/" + $(this).data('id'),
            method: 'GET',
            data: { id: $(this).data('id') },
            success: function (result) {
                $('#{singular}-view-file').html(result.html);
            },
			error: function(result){
				console.log('ERRO');
			}
        });
    });

});
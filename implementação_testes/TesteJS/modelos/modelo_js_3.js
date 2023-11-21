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

var {plural}_selects = [];
var {singular}_id;

$('body').on('click', '.{singular}_checkbox', function (e) {
var arrayChecked = []
var checkboxesMarcados = $("input[type='checkbox']:checked");
checkboxesMarcados.each(function () { arrayChecked.push($(this).val());});

{plural}_selects = arrayChecked;
{plural}_selects.length > 0 ? $('#bt-delete-{plural}').removeAttr('disabled') : $('#bt-delete-{plural}').attr('disabled', 'disabled');
})

$('body').on('click', '#bt-view-file', function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/{plural}-view-file/" + $(this).data('id'),
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

$('body').on('click', '#bt-delete-{singular}', function () { {singular}_id = $(this).data('id') })
$('#submit-delete-{singular}').click(function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/{plural}",
    method: 'DELETE',
    data:{ids: JSON.stringify({singular}_id)},
    headers: { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') },
    success: function (result) {
        console.log(result);
        $('#dt-{plural}').DataTable().ajax.reload();
        $('.alert-success').hide();
        //$('#deletarFeriado').modal('hide');
        window.location = document.URL;
    },
    error: function(result){
        $('.alert-danger').show();
           $('.alert-danger').append('<strong>Erro!</strong>&nbsp; ' + result.error + '');
        hideLoading('#loading-create-{singular}', '#loading-content-create-{singular}');
    }
});
});

$('body').on('click', '#bt-edit', function (e) {
e.preventDefault();
$.ajax({
    url: "/admin/{plural}/" + $(this).data('id'),
    method: 'GET',
    success: function (result) {
        $('#id-{singular}').val(1);
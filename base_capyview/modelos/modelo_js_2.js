    $('#{singular}-data').val('');
    $('#{singular}-companion').val('');
}

$(window).on('load', function(){
$('#cid').select2();
var inputSearch;
var timeout = null;
var blockKeyCodes = [16, 17, 18, 20, 27, 32, 33, 34, 37, 38, 39, 40, 91, 92, 93, 144];

var table = $('#dt-{{plural}}').DataTable({
    processing: true,
    serverSide: true,
    autoWidth: false,
    pageLength: 5,
    searchDelay: 1000,
    order: [[ 1, "desc" ]],
    lengthMenu: [5, 10, 25, 50],
    columnDefs: [{ "targets": 0, "orderable": false },{ "targets": 4, "orderable": false }],
    ajax: { url:"get-{{plural}}" },
    columns: [ 
        { data: 'checkbox', sClass: 'text-center', serachable: false },

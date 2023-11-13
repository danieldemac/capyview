<?
use App\Models\tabela_example;

Route::get('/tabela_examples', function () {
    $content = "Rota tabela_example criada.";
    return view('tabela_examples.index');
});
Route::get('get-tabela_examples', [tabela_exampleController::class, 'getAll'])->middleware('auth');
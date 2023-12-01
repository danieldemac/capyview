<?
use App\Http\Controllers\tabela_testeController;

// Rota para exibir o formulário de criação do modelo
Route::get('/tabela_testes/create', function () {
    $content = "Rota tabela_teste criada.";
    return view('tabela_testes.create');
})->name('tabela_testes.create');

Route::group(['prefix' => 'admin'], function () {
    Voyager::routes();

    
// Rota para armazenar um novo tabela_teste criado
Route::post('/tabela_testes', [tabela_testeController::class, 'store'])->name('tabela_testes.store');

// Rota para exibir detalhes de um tabela_teste específico
Route::get('/tabela_testes/{id}', [tabela_testeController::class, 'show'])->name('tabela_testes.show');

// Rota para exibir o formulário de edição de um tabela_teste específico
Route::get('/tabela_testes/{id}/edit', [tabela_testeController::class, 'edit'])->name('tabela_testes.edit');

// Rota para atualizar um tabela_teste específico
Route::put('/tabela_testes/{id}', [tabela_testeController::class, 'update'])->name('tabela_testes.update');
Route::patch('/tabela_testes/{id}', [tabela_testeController::class, 'update']);

// Rota para excluir um tabela_teste específico
Route::delete('/tabela_testes/{id}', [tabela_testeController::class, 'destroy'])->name('tabela_testes.destroy');

});

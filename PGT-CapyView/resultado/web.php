<?
use App\Http\Controllers\tabela_rafaelController;

// Rota para exibir o formulário de criação do modelo
Route::get('/tabela_rafaels/create', function () {
    $content = "Rota tabela_rafael criada.";
    return view('tabela_rafaels.create');
})->name('tabela_rafaels.create');

Route::group(['prefix' => 'admin'], function () {
    Voyager::routes();

    
// Rota para armazenar um novo tabela_rafael criado
Route::post('/tabela_rafaels', [tabela_rafaelController::class, 'store'])->name('tabela_rafaels.store');

// Rota para exibir detalhes de um tabela_rafael específico
Route::get('/tabela_rafaels/{id}', [tabela_rafaelController::class, 'show'])->name('tabela_rafaels.show');

// Rota para exibir o formulário de edição de um tabela_rafael específico
Route::get('/tabela_rafaels/{id}/edit', [tabela_rafaelController::class, 'edit'])->name('tabela_rafaels.edit');

// Rota para atualizar um tabela_rafael específico
Route::put('/tabela_rafaels/{id}', [tabela_rafaelController::class, 'update'])->name('tabela_rafaels.update');
Route::patch('/tabela_rafaels/{id}', [tabela_rafaelController::class, 'update']);

// Rota para excluir um tabela_rafael específico
Route::delete('/tabela_rafaels/{id}', [tabela_rafaelController::class, 'destroy'])->name('tabela_rafaels.destroy');

});

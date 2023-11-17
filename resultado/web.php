<?
use App\Http\Controllers\tabela_exampleController;

// Rota para exibir o formulário de criação do modelo
Route::get('/tabela_examples/create', function () {
    $content = "Rota tabela_example criada.";
    return view('tabela_examples.create');
})->name('tabela_examples.create');

// Rota para armazenar um novo tabela_example criado
Route::post('/tabela_example', [tabela_exampleController::class, 'store'])->name('tabela_examples.store');

// Rota para exibir detalhes de um tabela_example específico
Route::get('/tabela_example/{id}', [tabela_exampleController::class, 'show'])->name('tabela_examples.show');

// Rota para exibir o formulário de edição de um tabela_example específico
Route::get('/tabela_example/{id}/edit', [tabela_exampleController::class, 'edit'])->name('tabela_examples.edit');

// Rota para atualizar um tabela_example específico
Route::put('/tabela_example/{id}', [tabela_exampleController::class, 'update'])->name('tabela_examples.update');
Route::patch('/tabela_example/{id}', [tabela_exampleController::class, 'update']);

// Rota para excluir um tabela_example específico
Route::delete('/tabela_example/{id}', [tabela_exampleController::class, 'destroy'])->name('tabela_examples.destroy');

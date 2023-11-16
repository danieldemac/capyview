<?
use App\Http\Controllers\{singular}Controller;

// Rota para exibir o formulário de criação do modelo
Route::get('/{plural}/create', function () {
    $content = "Rota {singular} criada.";
    return view('{plural}.create');
})->name('{plural}.create');

// Rota para armazenar um novo {singular} criado
Route::post('/{singular}', [{singular}Controller::class, 'store'])->name('{plural}.store');

// Rota para exibir detalhes de um {singular} específico
Route::get('/{singular}/{id}', [{singular}Controller::class, 'show'])->name('{plural}.show');

// Rota para exibir o formulário de edição de um {singular} específico
Route::get('/{singular}/{id}/edit', [{singular}Controller::class, 'edit'])->name('{plural}.edit');

// Rota para atualizar um {singular} específico
Route::put('/{singular}/{id}', [{singular}Controller::class, 'update'])->name('{plural}.update');
Route::patch('/{singular}/{id}', [{singular}Controller::class, 'update']);

// Rota para excluir um {singular} específico
Route::delete('/{singular}/{id}', [{singular}Controller::class, 'destroy'])->name('{plural}.destroy');

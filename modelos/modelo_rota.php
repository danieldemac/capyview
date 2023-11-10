<?
use App\Models\{singular};

Route::get('/{plural}', function () {
    $content = "Rota {singular} criada.";
    return view('{plural}.index');
});
Route::get('get-{plural}', [{singular}Controller::class, 'getAll'])->middleware('auth');
<?
use App\Models\user_dependent;

Route::get('/user_dependents', function () {
    $content = "Rota user_dependent criada.";
    return view('user_dependents.index');
});
Route::get('get-user_dependents', [user_dependentController::class, 'getAll'])->middleware('auth');
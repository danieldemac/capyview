<?php

use App\Http\Controllers\AttestationController;
use App\Http\Controllers\CollaboratorController;
use App\Http\Controllers\PaymentController;
use App\Http\Controllers\VaccineController;
use App\Mail\Notification;
use App\Mail\TestAmazonSes;
use App\Models\Attestation;
use App\Models\Protheus;
use Illuminate\Support\Facades\Mail;
use Illuminate\Support\Facades\Route;
use TCG\Voyager\Facades\Voyager;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/e', function () {
    $content = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA Sejas Bem vindo ao portal do Colaborador, uma ferramenta desenvolvida para todos os que contribuem para essa empresa. 
    Clique no botão abaixo para acesso e conferir !!!";
    return view('emails.notification',['content'=>$content]);
});

Route::get('/email', function () {
    $content = "Seja Bem vindo ao portal do Colaborador, uma ferramenta desenvolvida para todos os que contribuem para essa empresa. 
    Clique no botão abaixo para acesso e conferir !!!";

    Mail::to('joao.martins@datametrica.com.br', 'João Martins')->send(new Notification('Bem-vindo ao Portal do Colaborador', $content, 'emails.notification'));
});


Route::group(['prefix' => 'admin'], function () {
    Voyager::routes();

    // COLABORADORES
    Route::get('/collaborators', function () {
        return view('collaborators.index');
    });
    Route::get('get-collaborators', [CollaboratorController::class, 'getAll'])->middleware('auth');


    // VACINAS
    Route::get('/vaccines', function () {
        return view('vaccines.index');
    });
    Route::get('get-vaccines', [VaccineController::class, 'getAll'])->middleware('auth');

    Route::post('/vaccines', [VaccineController::class, 'create'])->middleware('auth');


    // VACINAS GESTÃO
    Route::get('/management-vaccines', function () {
        return view('vaccines.management.index');
    });
    Route::get('get-management-vaccines', [VaccineController::class, 'getAll'])->middleware('auth');


    // ATESTADOS
    Route::get('/attestations', function () {
        return view('attestations.index');
    });
    Route::get('get-attestations', [AttestationController::class, 'getAll'])->middleware('auth');
    Route::post('/attestations', [AttestationController::class, 'updateOrCreate'])->middleware('auth');
    Route::get('attestations-view-file/{id}', [AttestationController::class, 'getViewFile'])->middleware('auth');
    Route::delete('/attestations', [AttestationController::class, 'destroy'])->middleware('auth');

    Route::get('attestations/{id}', function ($id) {
        return Attestation::find($id);
    });


    // ATESTADOS GESTÃO
    Route::get('/management-attestations', function () {
        return view('attestations.management.index');
    });
    Route::get('get-management-attestations', [AttestationController::class, 'getAll'])->middleware('auth');


    // PAGAMENTOS
    Route::get('/payments', function () {
        return view('payments.index');
    });
    Route::get('get-payments', [PaymentController::class, 'getAll'])->middleware('auth');

    Route::get('/management-payments', function () {
        return view('payments.management.index');
    });
    Route::get('get-management-payments', [PaymentController::class, 'getAll'])->middleware('auth');


    // DEPENDENTES
    Route::get('/dependents', function () {
        return view('dependents.index');
    });
    Route::get('get-dependents', [AttestationController::class, 'getAll'])->middleware('auth');
    Route::post('/dependents', [AttestationController::class, 'updateOrCreate'])->middleware('auth');
    Route::delete('/dependents', [AttestationController::class, 'destroy'])->middleware('auth');

    Route::get('dependents/{id}', function ($id) {
        return Attestation::find($id);
    });


    //
    Route::get('/protheus', function () {
        // '036078' - Luiz
        Protheus::getUserByCode('036078');
    });

  

});

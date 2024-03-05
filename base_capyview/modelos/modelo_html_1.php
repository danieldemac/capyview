@extends('voyager::master')
@section('page_title', 'Página criada - {singular}')

@section('page_header')
    <h1 class="page-title"><i class="icon voyager-receipt"></i>Nome {singular}</h1>
    <button class="btn btn-success btn-sm" type="button" data-toggle="modal" data-target="#modal-create-{singular}" id="bt-create-{singular}">
        <i class="voyager-plus"></i> Adicionar
    </button>
    <button class="btn btn-danger btn-sm" type="button" data-toggle="modal" data-target="#model-delete-{plural}" id="bt-delete-{plural}" disabled="true">
        <i class="voyager-trash"></i> Exclusão em massa
    </button>
@stop

@section('content')

<div class="panel panel-bordered">
    <div class="panel-body">
        <div class="row justify-content-center">
            <div class="card">
                <div class="card-body">
                    <div class="card-title"></div>
                    <table id="dt-{plural}" class="table table-bordered table-hover">
                        <thead>

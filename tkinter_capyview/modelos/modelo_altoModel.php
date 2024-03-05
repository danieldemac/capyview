<?php

namespace App\Models;

use Exception;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class UserDependent extends Model
{
    use HasFactory;

    protected $table      = {nome};
    protected $primaryKey = {num_aspasId};
    protected $fillable   = [{Text}{Booleano}{Numeric}];
    protected $dates      = [{Date}];

    public function getAll($search, $start, $limit, $order, $dir)
    {
        try {
            ${nome_semAspas} = static::select(DB::raw("name, relationship, birth"))
                            ->when($search !== false, function ($query) use ($search) {
                                $query->where(function($query) use ($search) {
                               
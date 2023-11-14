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
    protected $fillable   = [{Text}{Numeric}];
    protected $dates      = [{Date}];

    public function getAll($search, $start, $limit, $order, $dir)
    {
        try {
            $a = static::select(DB::raw("name, relationship, birth"))
                            ->when($search !== false, function ($query) use ($search) {
                                $query->where(function($query) use ($search) {
                                    {query_model}
                                });
                            })->where('id_user', Auth::user()->{num_Id});

            return [
                'count_data'=>$a->count(),
                'data'      =>$a->offset($start)->limit($limit)->orderBy($order, $dir)->get(), 
                'count_all' =>static::select(DB::raw("count({num_Id}) as count_all"))->get()->first()->count_all
            ];

        } catch(Exception $e) {
            dd($e);
        }
    }
}

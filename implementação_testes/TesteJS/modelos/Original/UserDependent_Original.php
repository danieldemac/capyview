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

    protected $table      = "user_dependents";
    protected $primaryKey = 'id';
    protected $fillable   = ['name', 'relationship', 'birth', 'id_user'];
    protected $dates      = ['created_at', 'updated_at', 'deleted_at'];

    public function getAll($search, $start, $limit, $order, $dir)
    {
        try {
            $a = static::select(DB::raw("name, relationship, birth"))
                            ->when($search !== false, function ($query) use ($search) {
                                $query->where(function($query) use ($search) {
                                    $query->where(DB::raw('lower(name)'), "LIKE", "%".$search."%") 
                                        ->orWhere(DB::raw('lower(relationship)'), "LIKE", "%".$search."%") 
                                        ->orWhere(DB::raw('lower(birth)'), "LIKE", "%".$search."%");
                                });
                            })->where('id_user', Auth::user()->id);

            return [
                'count_data'=>$a->count(),
                'data'      =>$a->offset($start)->limit($limit)->orderBy($order, $dir)->get(), 
                'count_all' =>static::select(DB::raw("count(id) as count_all"))->get()->first()->count_all
            ];

        } catch(Exception $e) {
            dd($e);
        }
    }
}

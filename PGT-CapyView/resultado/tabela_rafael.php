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

    protected $table      = "tabela_rafaels";
    protected $primaryKey = 'id';
    protected $fillable   = ['name', 'relationship', 'status','idade_filho'];
    protected $dates      = ['birth', 'created_at', 'updated_at', 'deleted_at'];

    public function getAll($search, $start, $limit, $order, $dir)
    {
        try {
            $tabela_rafaels = static::select(DB::raw("name, relationship, birth"))
                            ->when($search !== false, function ($query) use ($search) {
                                $query->where(function($query) use ($search) {
                                       $query->where('name', 'LIKE', "%".$search."%")
                                         ->orWhere('relationship', 'LIKE', "%".$search."%")
                                         ->orWhere('status', 'LIKE', "%".$search."%")
                                         ->orWhere('idade_filho', 'LIKE', "%".$search."%");
});
                            });

            return [
                'count_data'=>$tabela_rafaels->count(),
                'data'      =>$tabela_rafaels->offset($start)->limit($limit)->orderBy($order, $dir)->get(), 
                'count_all' =>static::select(DB::raw("count({num_Id}) as count_all"))->get()->first()->count_all
            ];

        } catch(Exception $e) {
            dd($e);
        }
    }
}

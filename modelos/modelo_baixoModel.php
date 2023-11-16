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

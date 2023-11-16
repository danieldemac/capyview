});
                            });

            return [
                'count_data'=>${nome}->count(),
                'data'      =>${nome}->offset($start)->limit($limit)->orderBy($order, $dir)->get(), 
                'count_all' =>static::select(DB::raw("count({num_Id}) as count_all"))->get()->first()->count_all
            ];

        } catch(Exception $e) {
            dd($e);
        }
    }
}

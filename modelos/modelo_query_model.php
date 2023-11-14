
                                    $query->where(DB::raw('lower(name)'),LIKE,%.$search.%)
                                          ->orWhere(DB::raw('lower(relationship)'),LIKE,%.$search.%);
                                          ->orWhere(DB::raw('lower(status)'),LIKE,%.$search.%);

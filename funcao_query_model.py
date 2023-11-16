def escrever_query(nomeSingular, valores):

    with open(f'resultado/{nomeSingular}.php', 'a+',  encoding='utf-8') as arquivo:
        if valores:
            arquivo.write(f" $query->where(DB::raw('lower({valores[0]})'),"+"LIKE"+","+"%"+".$search."+"%"+")\n")
            for valor in valores[1:]:
                arquivo.write(f"                                    ->orWhere(DB::raw('lower({valor})'),"+"LIKE"+","+"%"+".$search."+"%"+");\n")

        else:
            arquivo.write("Array vazia")
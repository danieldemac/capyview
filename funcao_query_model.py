def escrever_query(teste):
    with open('modelos/modelo_query_model.php', 'a+',  encoding='utf-8') as arquivo:
        if teste:
            arquivo.write(f"                                    $query->where(DB::raw('lower({teste[0]})'),"+"LIKE"+","+"%"+".$search."+"%"+")\n")
            for valor in teste[1:]:
                arquivo.write(f"                                          ->orWhere(DB::raw('lower({valor})'),"+"LIKE"+","+"%"+".$search."+"%"+");\n")

        else:
            arquivo.write("Array vazia")
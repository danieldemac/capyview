def escrever_query(nomeSingular, valores):
    with open(f'resultado/{nomeSingular}.php', 'a+', encoding='utf-8') as arquivo:
        if valores:
            for index, valor in enumerate(valores):
                if index == 0:
                    arquivo.write(f"        $query->where('{valor}', 'LIKE', \"%\".$search.\"%\")\n")
                elif index < len(valores) - 1:
                    arquivo.write(f"                                         ->orWhere('{valor}', 'LIKE', \"%\".$search.\"%\")\n")
                else:
                    arquivo.write(f"                                         ->orWhere('{valor}', 'LIKE', \"%\".$search.\"%\");\n")
        else:
            arquivo.write("Array vazia")
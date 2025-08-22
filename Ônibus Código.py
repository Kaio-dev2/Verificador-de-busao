buss_list = [ ]

with open('out.csv', 'r') as arquivo:
    for linha in arquivo.readlines():
        str_arr = linha.split(",")
        

        encontrado = False 
        for busao in buss_list:
            if str_arr[0] == busao["line"]:
                encontrado = True
                for parada in str_arr[1:]:
                    desembarcacao = parada.split(":")
                    busao["pass"] += int(desembarcacao[0])

        if not encontrado :
            buss_list.append({"line":str_arr[0], "pass":0})
            for busao in buss_list:
                if str_arr[0] == busao["line"]:
                    encontrado = True
                    for parada in str_arr[1:]:
                        desembarcacao = parada.split(":")
                        busao["pass"] += int(desembarcacao[0])
print(buss_list)

print(sorted(buss_list, key=lambda buss: buss["pass"], reverse=True))

maior = max(buss_list, key=lambda buss: buss["pass"])
menor = min(buss_list, key=lambda buss: buss["pass"])

print("\nMaior:", maior)
print("\nMenor:", menor)


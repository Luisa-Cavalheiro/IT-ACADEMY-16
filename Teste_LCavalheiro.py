
import csv

while True:
    print("MEDICAMENTOS NO BRASIL")
    data = []
    with open("TA_PRECO_MEDICAMENTO.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
    try:        
        menu1 = int(input(" Escolha a opção desejada:\n 1. Consultar medicamento\n 2. Gerar comparativo da lista de concessão de crédito tributário (PIS/COFINS)\n 3. Sair\n>>>"))
    except:
            print("Código inválido")
    if menu1 == 1:
        try:
            menu2 = int(input(
                "Escolha o dado para consulta:\n 1.Nome\n 2.Código de barras\n 3. Voltar ao menu principal\n>>>"))
        except:
            print("Código inválido")
        if menu2 == 1:
            entrada = input("Digite o nome do medicamento:\n>>>")
            convertUpper = entrada.upper()
            colunas = [x[0] for x in data]
            if convertUpper in colunas:
                for x in range(0, len(data)):
                    if (convertUpper == data[x][0]) and (data[x][38] == "Sim"):
                        print(data[x][0], data[x][8], data[x][9], data[x][13])
            else:
                print("Medicamento não encontrado")
        elif menu2 == 2:
            try:
                entrada = input("Digite o código de barras:\n>>>")
            except:
                print("Código inválido")
            colunas = [x[5] for x in data]
            if entrada in colunas:
                for x in range(0, len(data)):
                    if (entrada == data[x][5]):
                        valor1 = float(data[x][31].replace(',', '.'))
                        valor2 = float(data[x][23].replace(',', '.'))
                        saldo = valor1 - valor2
                        print(data[x][5], data[x][0], data[x][8], data[x][9],
                              data[x][13], data[x][23], data[x][31], round(saldo, 2))

            else:
                print("Medicamento não encontrado")
        elif menu2 == 3:
            continue
        else:
            print("Opção inválida.")

    elif menu1 == 2:        
        colunas = ([x][37] for x in data)
        negativas: int = 0
        neutras: int = 0
        positivas: int = 0

        for x in range(0, len(data)):
            if (data[x][37] == "Negativa"):
                negativas += 1
            elif (data[x][37] == "Neutra"):
                neutras += 1
            elif (data[x][37] == "Positiva"):
                positivas += 1
        
        per_neg = (100*negativas)/(negativas+positivas+neutras)
        per_pos = (100*positivas)/(negativas+positivas+neutras)
        per_neu = (100*neutras)/(negativas+positivas+neutras)
        
        grafico: str = ''
        ASTER = '*'
        
        for x in range(0, int(per_pos), 1):
            grafico: str = grafico + ASTER
       
        grafico1: str = ''
        for x in range(0, int(per_neg), 1):
            grafico1: str = grafico1 + ASTER
        
        grafico2: str = ''
        for x in range(0, int(per_neu), 1):
            grafico2: str = grafico2 + ASTER
        print("Positivas", round(per_pos, 2), "%", grafico)
        print("Negativas", round(per_neg, 2), "%", grafico1)
        print("Neutras", round(per_neu, 2), "%", grafico2)
    elif menu1 == 3:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida.")


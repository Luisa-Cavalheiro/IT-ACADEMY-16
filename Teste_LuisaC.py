# Importar a biblioteca csv para Python.
import csv

# Criar loop até o usuário encerrar.
while True:
    print("MEDICAMENTOS NO BRASIL")
# Criar array para carregar dados do csv
    data = []
# Abrir arquivo csv e dando alias
    with open("TA_PRECO_MEDICAMENTO.csv") as csvfile:
        # Ler arquivo csv e separando por ';'
        reader = csv.reader(csvfile, delimiter=';')
# Criar loop para ler arquivo
        for row in reader:
            # Popular array com os dados do arquivo csv
            data.append(row)
# Criar menu principal com entrada de dados
    menu1 = int(input(" Escolha a opção desejada:\n 1. Consultar medicamento\n 2. Gerar comparativo da lista de concessão de crédito tributário (PIS/COFINS)\n 3. Sair\n>>>"))
# Verificar se valor de entrada na variável menu1 é igual 1
    if menu1 == 1:
        # Criar entrada para submenu
        menu2 = int(input(
            "Escolha o dado para consulta:\n 1.Nome\n 2.Código de barras\n 3. Voltar ao menu principal\n>>>"))
# Verificar se valor inserido na variável menu2 é igual 1 no submenu
        if menu2 == 1:
            # captura valor de entrada
            entrada = input("Digite o nome do medicamento:\n>>>")
# transforma valor da variável entrada em letras maiusculas
            convertUpper = entrada.upper()
# faz loop na coluna 0 do array data e atribui valor a variável colunas
            colunas = [x[0] for x in data]
# verifica se valor da variável convertUpper está contido em colunas
            if convertUpper in colunas:
                # faz loop no array data que contém copia do arquivo
                for x in range(0, len(data)):
                    # verifica se valor da variavel convertUpper é igual a valor do array data na linha x coluna 0 E se valor do array data na linha x coluna 38 é igual a Sim
                    if (convertUpper == data[x][0]) and (data[x][38] == "Sim"):
                        # entrando na condição acima printa o valor na tela
                        print(data[x][0], data[x][8], data[x][9], data[x][13])
# caso valor da variável convertUpper não estiver contido em colunas faz o print da mensagem
            else:
                print("Medicamento não encontrado")
# Verificar se valor inserido na variável menu2 é igual 2 no submenu
        elif menu2 == 2:
            # Verifica se valor inputado e válido se sim segue o fluxo caso não for entra em except e faz print da mensagem
            try:
                entrada = input("Digite o código de barras:\n>>>")
            except:
                print("Código inválido")
# faz loop na coluna 5 do array data e atribui valor a variável colunas
            colunas = [x[5] for x in data]
# verifica se valor da variável entrada está contido em colunas
            if entrada in colunas:
                # faz loop no array data que contém copia do arquivo
                for x in range(0, len(data)):
                    # verifica se valor da variavel convertUpper é igual a valor do array data na linha x coluna 5
                    if (entrada == data[x][5]):
                        # converte dado para float e faz o replace de virgulas por um ponto, por fim atribui valor a variável valor1
                        valor1 = float(data[x][31].replace(',', '.'))
# converte dado para float e faz o replace de virgulas por um ponto, por fim atribui valor a variável valor2
                        valor2 = float(data[x][23].replace(',', '.'))
# calcula valor
                        saldo = valor1 - valor2
# mostra as informações no console  e faz arredondamento do valor saldo deixando somente 2 casas após a virgula
                        print(data[x][5], data[x][0], data[x][8], data[x][9],
                              data[x][13], data[x][23], data[x][31], round(saldo, 2))
# caso valor da variável entrada não estiver contido em colunas faz o print da mensagem
            else:
                print("Medicamento não encontrado")
# Verificar se valor inserido na variável menu2 é igual 3 no submenu e retorna para o menu1
        elif menu2 == 3:
            continue
# Verificar se valor inserido na variável menu2 é diferente de 1,2 ou 3
        else:
            print("Opção inválida.")
# Verificar se valor de entrada na variável menu1 é igual 2
    elif menu1 == 2:
        # faz loop nas linhas da coluna 37 do array data
        colunas = ([x][37] for x in data)
# declaraçao de variáveis para contabilização
        negativas: int = 0
        neutras: int = 0
        positivas: int = 0
# faz loop no array data
        for x in range(0, len(data)):
            # verifica se valor da linha x coluna 37 é igual a Negativa
            if (data[x][37] == "Negativa"):
                # realizar contabilização de valores negativos
                negativas += 1
    # verifica se valor da linha x coluna 37 é igual a  Neutra
            elif (data[x][37] == "Neutra"):
                # realizar contabilização de valores neutras
                neutras += 1
    # verifica se valor da linha x coluna 37 é igual a Positiva
            elif (data[x][37] == "Positiva"):
                # realizar contabilização de valores positivos
                positivas += 1
        # Realiza calculo da porcentagem para os valores
        per_neg = (100*negativas)/(negativas+positivas+neutras)
        per_pos = (100*positivas)/(negativas+positivas+neutras)
        per_neu = (100*neutras)/(negativas+positivas+neutras)
        # declaração de variável  e constante
        grafico: str = ''
        ASTER = '*'
        # Faz conversão da variável per_pos para inteiro e faz loop enquando valor da variável per_pos for menor ou igual ao indice
        for x in range(0, int(per_pos), 1):
            # faz a concatenação da variável aster a variável grafico em cada passagem do loop
            grafico: str = grafico + ASTER
        # declaração de variável
        grafico1: str = ''
        # Faz conversão da variável per_neg para inteiro e faz loop enquando valor da variável per_neg for menor ou igual ao indice
        for x in range(0, int(per_neg), 1):
            # faz a concatenação da variável aster a variável grafico em cada passagem do loop
            grafico1: str = grafico1 + ASTER
        # declaração de variável
        grafico2: str = ''
        # Faz conversão da variável per_neu para inteiro e faz loop enquando valor da variável per_neu for menor ou igual ao indice
        for x in range(0, int(per_neu), 1):
            # faz a concatenação da variável aster a variável grafico em cada passagem do loop
            grafico2: str = grafico2 + ASTER
        # apresenta resultado no console
        print("Positivas", round(per_pos, 2), "%", grafico)
        print("Negativas", round(per_neg, 2), "%", grafico1)
        print("Neutras", round(per_neu, 2), "%", grafico2)
# Verificar se valor de entrada na variável menu1 é igual 3 e encerra o programa
    elif menu1 == 3:
        print("Programa encerrado")
        break
# Verificar se valor de entrada na variável menu1 é diferente de 1,2 ou 3 faz o print da mensagem
    else:
        print("Opção inválida.")


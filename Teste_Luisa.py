print ("CONSULTA DE MEDICAMENTOS")
import csv
data=[]
with open("TA_PRECO_MEDICAMENTO.csv") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        data.append(row)
print(data)

entrada= input("Digite o nome do medicamento: ")
col=[x[0] for x in data]
if entrada in col:
    for x in range(0,len(data)):
        if entrada==data[x][0]:
            print (data[x])
else:
    print("Medicamento não encontrado")
    

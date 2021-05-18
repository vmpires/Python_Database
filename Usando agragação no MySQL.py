import pymysql
import json

f = open ('config.json', 'r')
key = json.load(f)

# Iniciando a conexão
conexao = pymysql.connect(host="localhost", db="vstore", user="root", passwd=key['key'])

# Gerando o cursor

cursor = conexao.cursor()

# QUERY + impressão
cursor.execute('SELECT nome,idade FROM cliente ORDER BY idade ASC;')
listaordenada = cursor.fetchall()

for item in listaordenada:
    print(item)

print(f'O cliente com menor idade é o {listaordenada[0][0]} e ele tem {listaordenada[0][1]} anos.')
print(f'O cliente com maior idade é o {listaordenada[-1][0]} e ele tem {listaordenada[-1][1]} anos.')

# Executando as transações
conexao.commit()

#Finalizando a conexão
conexao.close()
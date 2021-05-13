import pymysql
import json

f = open ('config.json', 'r')
key = json.load(f)

# Iniciando a conexão
conexao = pymysql.connect(host="localhost", db="vstore", user="root", passwd=key['key'])

# Gerando o cursor
cursor = conexao.cursor()
cursor.execute('SELECT * FROM Cliente;')
myresult = cursor.fetchall()

# Executar a transação
for item in myresult:
    print(item)

# Executando as transações
conexao.commit()

#Finalizando a conexão
conexao.close()
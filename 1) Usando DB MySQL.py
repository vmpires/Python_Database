import pymysql
import json

f = open ('config.json', 'r')
key = json.load(f)

# Iniciando a conexão
conexao = pymysql.connect(host="localhost", db="vstore", user="root", passwd=key['key'])

# Gerando o cursor
cursor = conexao.cursor()

cursor.execute('SELECT v.id_venda as Venda, c.nome as Cliente, p.nome as Produto, \
    vp.quantidade as Quantidade \
    FROM vendacliente as v \
    JOIN cliente as c \
    ON v.id_cliente = c.id_cliente \
    JOIN vendaproduto as vp \
    ON v.id_venda = vp.id_venda \
    JOIN produto as p ON vp.id_produto = p.id_produto;')

myresult = cursor.fetchall()

# Executar a transação
for item in myresult:
    print(item)

# Executando as transações
conexao.commit()

#Finalizando a conexão
conexao.close()
# 2) Com a conexão criada, selecione na tabela tabela_treinamento do banco:
# 
# a) As linhas que correspondem a pessoas de São Paulo

host = "localhost"
port = 5432
db = "postgres"
user = "postgres"
passwd = "postgres"


import psycopg2
import pandas as pd

query = '''SELECT *
        FROM "QQTech"."treinamento" 
       where "cidade" = 'São Paulo' '''

with psycopg2.connect(
    host = host,
    dbname = db,
    port = port,
    user = user,
    password = passwd
    ) as conn:
    
    df = pd.read_sql(query, conn)
    
print(df)

# b) As linhas que correspondem a pessoas com idade entre 22 e 27 anos

query = '''SELECT *
        FROM "QQTech"."treinamento" 
       WHERE idade >= 22 AND idade <= 27
       ORDER BY idade asc'''
df = pd.read_sql(query, conn)

print(df)

# c) As cidades das pessoas com o nome Maria

query = '''SELECT cidade
        FROM "QQTech"."treinamento" 
       WHERE nome = 'Maria'
    '''
df = pd.read_sql(query, conn)

print(df)
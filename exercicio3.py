# 3) Insira na tabela 2 novas linhas com dados ficticios

host = "localhost"
port = 5432
db = "postgres"
user = "postgres"
passwd = "postgres"

import psycopg2

cmd = '''INSERT INTO "QQTech"."treinamento"
        ("nome", "idade","cidade") VALUES (%s, %s,%s)'''
values = [("Allan", 32,"Recife"),("Luana", 20,"Aratu")]

with psycopg2.connect(
    host = host,
    dbname = db,
    port = port,
    user = user,
    password = passwd
    ) as conn:
    
    with conn.cursor() as cursor:
        cursor.executemany(cmd, values)
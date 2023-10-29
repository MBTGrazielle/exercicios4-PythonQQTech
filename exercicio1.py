# 1) Crie uma conexão com o banco QQ TECH.

host = "localhost"
port = 5432
db = "postgres"
user = "postgres"
passwd = "postgres"


import psycopg2

with psycopg2.connect(
    host = host,
    dbname = db,
    port = port,
    user = user,
    password = passwd
    ) as conn:
    
    print('Conexão estabelecida')
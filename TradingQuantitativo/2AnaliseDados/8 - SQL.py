# Data: 27/06/2025
# Instalar a extensão SQLite

import sqlite3
import pandas as pd

# Cria uma base de dados
conn = sqlite3.connect('Dados/web.db')

# Importa o .csv
# Vive em memória RAM
df = pd.read_csv('Dados/bd_data.csv', index_col =0)
df.index.name ='index_name'

# Exporta o df para a base de dados SQL
# Salva no HD
df.to_sql('data',conn,index_label='index_name')

# Envia comandos para o SQL
c = conn.cursor()

# Cria uma tabela
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()

# Deleta a tabela
c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

# Cria uma tabela
c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
conn.commit()




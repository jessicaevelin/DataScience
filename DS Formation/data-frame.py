import pandas as pd
usuarios = {
	"nome" : ["Meigarom", "Claudio", "Fernando", "Diego", "André"],
	"idade" : [34, 30, 36, 25, 36],
	"cidade" : ["Indaiatuba", "Arcos", "Ouro Fino", "Itapira", "Curitiba"],
	"estado": ["SP", "RJ", "SP", "RJ", "RJ"]
	}
df = pd.DataFrame(usuarios)

print(df)
"""        
nome  idade      cidade estado
0  Meigarom     34  Indaiatuba     SP
1   Claudio     30       Arcos     RJ
2  Fernando     36   Ouro Fino     SP
3     Diego     25     Itapira     RJ
4     André     36    Curitiba     RJ 
"""

# Seleciona a primeira linha e primeira coluna 
df_selecionado = df.iloc[0, 0]
print( df_selecionado ) 
""" 
Meigarom 
"""

# Selecionar primeira linha e um intervalo de coluna 
df_selecionado = df.iloc[0, 1:3] 
print( df_selecionado) 
""" 
idade             34
cidade    Indaiatuba
Name: 0, dtype: object
"""

 # Selecionar um intervalo de linha e uma coluna 
df_selecionado = df.iloc[0:9999, 3] 
print( df_selecionado ) 
""" 
0    SP
1    RJ
2    SP
3    RJ
4    RJ
Name: estado, dtype: object 
"""

# Selecionar um intervalo de linha e um intervalo de coluna 
df_selecionado = df.iloc[0:99999, 2:99999] 
print( df_selecionado ) 
""" 
    cidade estado
0  Indaiatuba     SP
1       Arcos     RJ
2   Ouro Fino     SP
3     Itapira     RJ
4    Curitiba     RJ
"""

# Selecionar um intervalo de linha e uma coluna pelo nome 
df_selecionado = df.loc[1:2,"cidade"] 
print( df_selecionado ) 
""" 
1        Arcos
2    Ouro Fino
Name: cidade, dtype: object
"""

# Selecionar um intervalo de linha e várias coluna pelo nome 
colunas = ["idade", "estado", "cidade"] 
df_selecionado = df.loc[3:25, colunas ] 
print( df_selecionado ) 
"""    
    idade estado    cidade
3     25     RJ   Itapira
4     36     RJ  Curitiba
"""
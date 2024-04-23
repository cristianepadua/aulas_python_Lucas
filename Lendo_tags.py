import matplotlib.pyplot as plt
import matplotlib as mpl
from time import sleep
import numpy as np
import pandas as pd

df = pd.read_excel('/Users/cristianeferreira/Downloads/Aulas Python/Analise Petições2.xlsx',sheet_name='Petições Analisadas')
df1 = df.to_dict('index')
print(df1[0]['TAG.1'])
print(df1[0])
#for item in df1[0]:
#    print(f"{item} = {df1[0][item]}\n")

rotulo_tags = ['TAG','TAG.1','TAG.2','TAG.3','TAG.4','TAG.5','TAG.6','TAG.7','TAG.8','TAG.9','TAG.10','TAG.11']
todas_tags = []
lista_total = []
adicionar_tag = []
tamanho = []
x = []
y = []

for item in df1:
    tamanho.append(df1[item]['PÁGINAS'])
print(tamanho)
print(len(tamanho))

for item in df1:
    #print(item)
    #sleep(0.2)
    for i in range(12):
        elemento = df1[item][rotulo_tags[i]]
        if type(elemento) is str:
            lista_total.append(elemento)
            if elemento not in todas_tags:
                todas_tags.append(elemento)
                adicionar_tag.append(elemento)
    x.append(item)
    y.append(len(adicionar_tag))
    adicionar_tag.clear()
print(x)
print()
print(y)
print(f"Não foi necessário criar  TAG nova em {(y.count(0))*100/350} % das petições anlisadas.")
print(f"Foram necessárias apenas {len(todas_tags)} TAGs diferentes para representar o conteúdo de {len(x)} petições.")
print(f"Em média, foram necessárias cerca de {len(lista_total)/len(x)} TAGs para representar o conteúdo de {len(x)} petições.")
y1 = []
soma = 0
for item in y:
    soma = soma + item
    y1.append(soma)
print(y1)
print(todas_tags)
print(lista_total)
print(len(lista_total))

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x,y1)  # Plot some data on the axes.
ax.set_xlabel("Número de petições analisadas")
ax.set_ylabel("Número total de TAGs utilizadas")
ax.set_title("Evolução da quantidade de TAGs por petição analisada")
plt.show()

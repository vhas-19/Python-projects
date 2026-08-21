import os
import pandas as pd
import matplotlib.pyplot as plt

os.system('cls')

arquivo = os.getcwd()+"\\aula_07\\arquivos\\copa_campeoes.xlsx"
df = pd.read_excel(arquivo)

df.set_index('Selecao')['Titulos'].plot.pie(
    autopct='%1.1f%%',
    startangle=140,
    figsize=(8,8),
    title='Proporção de Tituos Mundiais'
)

plt.show()
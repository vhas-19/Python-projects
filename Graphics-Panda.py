import os
import pandas as pd
import matplotlib.pyplot as plt

os.system('cls')

arquivo = os.getcwd()+"\\aula_07\\arquivos\\alunos_media.csv"
df = pd.read_csv(arquivo, sep=';')

plt.bar(df['Aluno'], df['Media'], color='skyblue')

plt.axhline(y=7.0, color='red', linestyle='--', label='Media de Aprovação')

plt.title('Desempenho da Turma - Médias Finais')
plt.xlabel('Alunos (x)')
plt.ylabel('Nota Final (y)')
plt.ylim(0,10)
plt.legend()

plt.show()
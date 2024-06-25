import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("games.csv")


# df.plot.hist(column="white_rating")
# plt.show()


# numero de vitorias
#victory_counts = df['victory_status'].value_counts()
#victory_counts.plot(kind='bar')
#plt.xlabel('victory status')
#plt.ylabel('number of games')
#plt.title('distribuição de status de vitoria')

## aberturas
#opening_counts = df['opening_eco'].value_counts()
#opening_counts.plot(kind='bar')
#plt.xlabel('opening code')
#plt.ylabel('number of games')
#plt.title('popularidade de diferentes aberturas')

# comparação de rating
# plt.scatter(df['white_rating'], df['black_rating'])
# plt.xlabel('white rating')
# plt.ylabel('black rating')
# plt.title('pontuação de brancas vs pretas')



plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv('EPL_20_21.csv')


print('shape of the data:',df.shape)
print('\n first five rows:',df.head())
print('\n first column names:')
print(df.columns.to_list())
print('\n total no of players:',len(df))
print('\n missing values:')
print(df.isnull().sum())



# CHART 1 — Top 10 Scorers

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('EPL_20_21.csv')

df['Total_Cards'] = df['Yellow_Cards'] + df['Red_Cards']

sns.set_style("darkgrid")
plt.figure(figsize=(12,6))




# CHART 1 — Top 10 Scorers



top_scorers = df[['Name', 'Club', 'Goals']].sort_values('Goals', ascending=False).head(10).reset_index(drop=True)
top_scorers.index = top_scorers.index + 1


ax = sns.barplot(data=top_scorers, x='Goals', y='Name', hue='Name', palette='Reds_r', legend=True)
plt.title('Top 10 Goal Scorers — EPL 2020/21')
plt.xlabel('Goals')
plt.ylabel('Player')
plt.tight_layout()
plt.savefig('top_scorers.png')
plt.show()



# CHART 2 — Top 10 Assist Leaders



top_assists = df[['Name', 'Club', 'Assists']].sort_values('Assists', ascending=False).head(10).reset_index(drop=True)




sns.barplot(data=top_assists, x='Assists', y='Name', hue='Name', palette='Blues_r', legend=True)
plt.title('Top 10 Assist Leaders — EPL 2020/21')
plt.xlabel('Assists')
plt.ylabel('Player')
plt.tight_layout()
plt.savefig('top_assists.png')
plt.show()




# CHART 3 — Most Aggressive Teams



aggressive_teams = df.groupby('Club')['Total_Cards'].sum().sort_values(ascending=False).head(10).reset_index()





sns.barplot(data=aggressive_teams, x='Total_Cards', y='Club', hue='Club', palette='Oranges_r', legend=True)
plt.title('Top 10 Most Aggressive Teams — EPL 2020/21')
plt.xlabel('Total Cards (Yellow + Red)')
plt.ylabel('Club')
plt.tight_layout()
plt.savefig('aggressive_teams.png')
plt.show()





# CHART 4 — Most Aggressive Nations



aggressive_nations = df.groupby('Nationality')['Total_Cards'].sum().sort_values(ascending=False).head(10).reset_index()




sns.barplot(data=aggressive_nations, x='Total_Cards', y='Nationality', hue='Nationality', palette='Purples_r', legend=True)
plt.title('Top 10 Most Aggressive Nationalities — EPL 2020/21')
plt.xlabel('Total Cards')
plt.ylabel('Nationality')
plt.tight_layout()
plt.savefig('aggressive_nations.png')
plt.show()




# CHART 5 — Defenders with Most Goals




defenders = df[df['Position'].str.contains('DF', na=False)]
top_def_scorers = defenders[['Name', 'Club', 'Goals']].sort_values('Goals', ascending=False).head(10).reset_index(drop=True)


sns.barplot(data=top_def_scorers, x='Goals', y='Name', hue='Name', palette='Greens_r', legend=True)
plt.title('Top 10 Goal Scoring Defenders — EPL 2020/21')
plt.xlabel('Goals')
plt.ylabel('Defender')
plt.tight_layout()
plt.savefig('defenders_goals.png')
plt.show()




# CHART 6 — Most Accurate Passers




outfield = df[~df['Position'].str.contains('GK|DF', na=False)]
outfield = outfield[outfield['Passes_Attempted'] > 100]
top_passers = outfield[['Name', 'Club', 'Perc_Passes_Completed']].sort_values('Perc_Passes_Completed', ascending=False).head(10).reset_index(drop=True)

plt.figure()
sns.barplot(data=top_passers, x='Perc_Passes_Completed', y='Name', hue='Name', palette='YlOrBr', legend=True)
plt.title('Top 10 Most Accurate Passers (MF & FW) — EPL 2020/21')
plt.xlabel('Pass Completion %')
plt.ylabel('Player')
plt.tight_layout()
plt.savefig('accurate_passers.png')
plt.show()



import pandas as pd

df = pd.read_csv('data/music_project_en.csv')
        
def replace_wrong_genres(df, column, wrong_genres, correct_genre):
    for wrong_genre in wrong_genres:
        df[column] = df[column].replace(wrong_genre, correct_genre)   
    return df
# Função para substituir duplicados implícitos

def number_tracks(day, city):
    filtered_df = df[df['day'] == day]
    filtered_df = filtered_df[filtered_df['city'] == city]

    count = filtered_df['user_id'].count()
    
    return count
# Função para calcular o número de músicas tocadas em determinado dia e cidade 

# Pré processamento de dados
# Renomeando columas automaticamente
new_col_names = []

for col in df.columns:
    name_lowered = col.lower()
    # Convertendo os nomes das colunas em minúsculo
    name_stripped = name_lowered.strip()
    # Removendo os espaços
    new_col_names.append(name_stripped)
    # Adicionando o novo nome à nova lista

df.columns = new_col_names
df = df.rename(columns= {'userid': 'user_id'})
# Alterando a coluna userid


columns_to_replace = ['track', 'artist', 'genre']
for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')
# Substituindo todos os valores ausentes pelo valor padrão 'unknown'


df.drop_duplicates(inplace=True)
# Eliminando todas as linhas duplicadas que contei com o método df.duplicated().sum()

wrong_genres = ['hip', 'hop', 'hip-hop']
correct_genre = 'hiphop'

df = replace_wrong_genres(df=df, column='genre', wrong_genres=wrong_genres, correct_genre=correct_genre)     
# Chamando a função para substituir duplicados implicitos

print("\nQuantidade de músicas tocadas por dia:")
print("\nMonday - Springfield =", number_tracks('Monday', 'Springfield'))
print("Monday - Shelbyville =", number_tracks('Monday', 'Shelbyville'))
print("\nWednesday - Springfield =", number_tracks('Wednesday', 'Springfield'))
print("Wednesday - Shelbyville =", number_tracks('Wednesday', 'Shelbyville'))
print("\nFriday - Springfield =", number_tracks('Friday', 'Springfield'))
print("Friday - Shelbyville =", number_tracks('Friday', 'Shelbyville'))
print('')
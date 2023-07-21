import pandas as pd

# crie um dataframe usando o arquivo final.csv
df = pd.read_csv('C:/Users/55719/Desktop/Pro Aulas Python/C142 PRO TODAS ATV/C142 PROF REF/final.csv')

# classificação de dataframe: em relação à coluna weighted_rating em ordem crescente
df = df.sort_values('weighted_rating' , ascending = False)

# dataframe final
output = df[['original_title' , 'poster_link' , 'runtime', 'release_date' , 'weighted_rating' ]].head(20)
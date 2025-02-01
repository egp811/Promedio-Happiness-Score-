import pandas as pd

# Cargar el dataset
df = pd.read_csv('WorldHappinessReport.csv')

# Calcular el promedio de la puntuación de felicidad por año
average_happiness_by_year = df.groupby('Year')['Happiness Score'].mean()

# Encontrar el país con la puntuación más alta y más baja cada año
max_happiness_by_year = df.loc[df.groupby('Year')['Happiness Score'].idxmax()]
min_happiness_by_year = df.loc[df.groupby('Year')['Happiness Score'].idxmin()]

# Mostrar los resultados
print("Promedio de la puntuación de felicidad por año:")
print(average_happiness_by_year)

print("\nPaís con la puntuación más alta cada año:")
print(max_happiness_by_year[['Year', 'Country', 'Happiness Score']])

print("\nPaís con la puntuación más baja cada año:")
print(min_happiness_by_year[['Year', 'Country', 'Happiness Score']])
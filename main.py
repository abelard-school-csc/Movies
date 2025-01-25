import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

if not os.path.exists('images'):
    os.makedirs('images')

df = pd.read_csv('movie.csv')
df['year'] = df['title'].str.extract(r'\((\d{4})\)')
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

df['genres_split'] = df['genres'].str.split('|')
all_genres = [genre for genres in df['genres_split'] for genre in genres]
genre_counts = pd.Series(all_genres).value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title('Most Common Movie Genres')
plt.xlabel('Number of Movies')
plt.tight_layout()
plt.savefig('images/genre_distribution.png')
plt.close()

movies_per_year = df['year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.plot(movies_per_year.index, movies_per_year.values)
plt.title('Number of Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.savefig('images/movies_per_year.png')
plt.close()

plt.figure(figsize=(12, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index)
plt.title('Most Common Movie Genres')
plt.xlabel('Number of Movies')
plt.tight_layout()
plt.savefig('images/genre_distribution.png')
plt.close()

movies_per_year = df['year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
plt.plot(movies_per_year.index, movies_per_year.values)
plt.title('Number of Movies Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.savefig('images/movies_per_year.png')
plt.close()

genre_combinations = df['genres'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=genre_combinations.values, y=genre_combinations.index)
plt.title('Top 10 Most Common Genre Combinations')
plt.xlabel('Number of Movies')
plt.tight_layout()
plt.savefig('images/genre_combinations.png')
plt.close()

avg_movies_per_year = df.groupby('year').size().mean()
total_movies = len(df)
total_unique_genres = len(genre_counts)
total_years = df['year'].nunique()

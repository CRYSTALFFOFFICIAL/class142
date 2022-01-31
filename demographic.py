import pandas as pd
import csv
import numpy as np

df2 = pd.read_csv("final.csv")

C = df2['vote_average'].mean()

m = df2['vote_count'].quantile(0.9)

q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)
output = q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10).values.tolist()


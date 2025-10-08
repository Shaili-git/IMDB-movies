import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Welcome to the dataset page")
st.write("This page contains the datasets used in the analysis.")

st.subheader("Netflix Dataset")
df = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\IMDB movies\pages\imdb_top_1000.csv")
df



# Top 20 Movies by IMDB Rating (Bar Chart)
st.subheader("Top 20 Movies by IMDB Rating")
top_20_movies = df.nlargest(20, 'IMDB_Rating')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='IMDB_Rating', y='Series_Title', data=top_20_movies, ax=ax, palette='viridis')
ax.set_title('Top 20 Movies by IMDB Rating')
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('Movie Title')
st.pyplot(fig)

#  Distribution of IMDB Ratings (Histogram)
st.subheader("Distribution of IMDB Ratings")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['IMDB_Rating'], bins=20, kde=True, ax=ax, color='skyblue')
ax.set_title('Distribution of IMDB Ratings')
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('Frequency')
st.pyplot(fig)

#  Movie Count by Genre (Bar Chart)
st.subheader("Movie Count by Genre")
genre_counts = df['Genre'].value_counts().head(10)  
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index, ax=ax, palette='magma')
ax.set_title('Top 10 Movie Genres by Count')
ax.set_xlabel('Number of Movies')
ax.set_ylabel('Genre')
st.pyplot(fig)

#  Average IMDB Rating by Genre (Bar Chart)
st.subheader("Average IMDB Rating by Genre")
avg_rating_by_genre = df.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_rating_by_genre.values, y=avg_rating_by_genre.index, ax=ax, palette='coolwarm')
ax.set_title('Top 10 Genres by Average IMDB Rating')
ax.set_xlabel('Average IMDB Rating')
ax.set_ylabel('Genre')
st.pyplot(fig)

#  Average Gross by Genre (Bar Chart)
st.subheader("Average Gross by Genre")
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')
avg_gross_by_genre = df.groupby('Genre')['Gross'].mean().sort_values(ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_gross_by_genre.values, y=avg_gross_by_genre.index, ax=ax, palette='spring')
ax.set_title('Top 10 Genres by Average Gross')
ax.set_xlabel('Average Gross')
ax.set_ylabel('Genre')
st.pyplot(fig)

# Runtime Distribution (Histogram)
st.subheader("Runtime Distribution")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['Runtime'], bins=20, kde=True, ax=ax, color='lightgreen')
ax.set_title('Distribution of Movie Runtimes')
ax.set_xlabel('Runtime (minutes)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

#  Gross vs IMDB Rating (Scatter Plot)
st.subheader("Gross vs IMDB Rating")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='IMDB_Rating', y='Gross', data=df, ax=ax, hue='Genre', palette='tab10', alpha=0.7)
ax.set_title('Gross vs IMDB Rating')
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('Gross')
st.pyplot(fig)


# No_of_votes vs IMDB Rating (Scatter Plot)
st.subheader("No_of_votes vs IMDB Rating")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='IMDB_Rating', y='No_of_Votes', data=df, ax=ax, hue='Genre', palette='tab10', alpha=0.7)
ax.set_title('No_of_votes vs IMDB Rating')
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('No_of_votes')
st.pyplot(fig)

#No_of_votes vs IMDB Rating (Scatter Plot)
st.subheader("No_of_votes vs IMDB Rating")   
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='IMDB_Rating', y='No_of_Votes', data=df
, ax=ax, hue='Genre', palette='tab10', alpha=0.7)
ax.set_title('No_of_votes vs IMDB Rating')  
ax.set_xlabel('IMDB Rating')
ax.set_ylabel('No_of_votes')
st.pyplot(fig)

#Top 10 Directors by Gross Earnings (Bar Chart)
st.subheader("Top 10 Directors by Gross Earnings")
top_directors = df.groupby('Director')['Gross'].sum().nlargest(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, ax=ax
, palette='autumn')
ax.set_title('Top 10 Directors by Gross Earnings')  
ax.set_xlabel('Total Gross Earnings')
ax.set_ylabel('Director')   
st.pyplot(fig)  

#IMDB Rating Trend by Released Year (Line Chart)
st.subheader("IMDB Rating Trend by Released Year")
rating_trend = df.groupby('Released_Year')['IMDB_Rating'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=rating_trend.index, y=rating_trend.values, ax=ax, marker='o', color='purple')
ax.set_title('IMDB Rating Trend by Released Year')
ax.set_xlabel('Released Year')
ax.set_ylabel('Average IMDB Rating')
st.pyplot(fig)

# Gross Trend by Released Year (Line Chart)
st.subheader("Gross Trend by Released Year")
gross_trend = df.groupby('Released_Year')['Gross'].mean()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=gross_trend.index, y=gross_trend.values, ax=ax, marker='o', color='orange')
ax.set_title('Gross Trend by Released Year')
ax.set_xlabel('Released Year')
ax.set_ylabel('Average Gross')
st.pyplot(fig)

#Most Frequent Actors (Bar Chart)

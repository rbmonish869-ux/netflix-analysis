import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="type", palette="Set2")
plt.title("Movies vs TV Shows on Netflix")
plt.savefig("movies_vs_tvshows.png")
plt.show()

# Top 10 Genres
plt.figure(figsize=(10,5))
df['listed_in'].str.split(',').explode().str.strip().value_counts()[:10].plot(kind="bar")
plt.title("Top 10 Genres on Netflix")
plt.ylabel("Count")
plt.savefig("top_genres.png")
plt.show()

# Content Ratings Distribution
plt.figure(figsize=(8,4))
df['rating'].value_counts().head(10).plot(kind="bar", color="skyblue")
plt.title("Content Ratings Distribution")
plt.ylabel("Count")
plt.savefig("ratings_dist.png")
plt.show()

# Year-wise Releases
df['release_year'].value_counts().sort_index().plot(kind="line", figsize=(10,5))
plt.title("Number of Releases per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("releases_per_year.png")
plt.show()

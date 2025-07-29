# Movie-Recommendation-System-using-Python

🎬 Movie Recommendation System
This is a content-based Movie Recommendation System built using Python. It recommends movies based on similarity in content (like genre, keywords, overview, cast, etc.) using vectorization techniques and cosine similarity.

🔍 Overview
This project aims to help users discover movies similar to the ones they already like. The system analyzes various textual features of movies and suggests recommendations using machine learning techniques. It uses content-based filtering, meaning it focuses solely on movie features rather than user ratings.

🛠️ Technologies Used
Python

Pandas – for data manipulation

NumPy – for numerical operations

Scikit-learn – for vectorization and similarity calculations

NLTK – for text preprocessing

Jupyter Notebook – for implementation and analysis

📁 Dataset
The project uses two combined datasets:

tmdb_5000_movies.csv

tmdb_5000_credits.csv

These datasets include information like movie titles, genres, cast, crew, keywords, and overviews.

📌 Key Features
Preprocessing and cleaning of movie metadata

Extraction and combination of important features (genre, cast, crew, etc.)

Tokenization, stemming, and removal of stopwords

Feature vectorization using CountVectorizer

Similarity computation using Cosine Similarity

Function to recommend top 5 similar movies based on input title

✅ How It Works
Load and merge the movie and credits datasets.

Extract and engineer important features into a new column called tags.

Preprocess text data (lowercase, remove spaces, stemming).

Convert text into vectors using CountVectorizer.

Compute cosine similarity between movie vectors.

Recommend top similar movies using similarity scores.

🧪 Sample Usage
python
Copy
Edit
recommend('Avatar')
Output:

markdown
Copy
Edit
1. John Carter  
2. Guardians of the Galaxy  
3. The Avengers  
4. The Legend of Tarzan  
5. Battleship
📦 Installation
Clone the repository and run the notebook:

bash
Copy
Edit
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
jupyter notebook

pip install pandas numpy scikit-learn nltk
📈 Future Enhancements
Add a web interface using Streamlit or Flask

Incorporate collaborative filtering or hybrid approaches

Deploy the model for public use

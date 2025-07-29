# Importing necessary libraries
import streamlit as st              # Streamlit for creating web app interface
import pickle                       # Pickle to load pre-saved Python objects (like model, data)
import pandas as pd                # Pandas for handling DataFrames

# Define a function to recommend movies based on cosine similarity
def recommended_movies(movie):
    # Find the index of the selected movie in the DataFrame
    movie_index = movies[movies['movie_title'] == movie].index[0]

    # Get similarity scores for that movie with all others
    distances = similarity[movie_index]

    # Sort the distances and get the top 5 most similar movies (excluding the movie itself)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Store recommended movie titles in a list
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].movie_title)
    return recommended_movies

# Load the pickled movie data (a list of dictionaries or records)
movies_list = pickle.load(open("C:/Users/Appa/PycharmProjects/Movie-RecommenderS-ystem/movies.pkl"
, 'rb'))

# Convert the loaded list into a pandas DataFrame
movies = pd.DataFrame(movies_list)

# Load the pickled similarity matrix
similarity_list = pickle.load(open("C:/Users/Appa/PycharmProjects/Movie-RecommenderS-ystem/similarity.pkl", 'rb'))

# Convert the similarity list into a DataFrame for easier indexing
similarity = pd.DataFrame(similarity_list)

# Extract just the list of movie titles for use in the dropdown
movies_list = movies['movie_title'].values

# Set the title of the Streamlit web application
st.title('Movie Recommender System')

# Create a dropdown menu (selectbox) with movie titles
selected_movie_name = st.selectbox("Movies List", movies_list)

# When the user clicks the "Recommend" button:
if st.button('Recommend'):
    # Call the recommendation function and get similar movies
    recommendations = recommended_movies(selected_movie_name)

    # Display each recommended movie title on the web page
    for i in recommendations:
        st.write(i)

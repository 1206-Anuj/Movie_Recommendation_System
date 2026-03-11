import streamlit as st
import pickle
import pandas as pd
import gzip

# load saved data
movies = pickle.load(open('movies.pkl','rb'))

with gzip.open('similarity.pkl.gz','rb') as f:
    similarity = pickle.load(f)


# recommendation function
def recommend(movie):
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
    recommended_movies = []
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies


# Streamlit UI
st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    
    recommendations = recommend(selected_movie)
    
    for movie in recommendations:
        st.write(movie)
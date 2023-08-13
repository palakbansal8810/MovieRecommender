import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

st.title('Movie Recommender System')

movies_dict=pickle.load(open('movie-recommendersystem/movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('movie-recommendersystem/similarity','rb'))

def fetch_posters(movie_id):

    url = "https://api.themoviedb.org/3/movie/{}?api_key=e1f1eccc1ed571dc33d46a0e0cf766a5&language=en-US".format(movie_id)

    response = requests.get(url)
    data=response.json()
    print(data)
    poster_url = 'https://image.tmdb.org/t/p/w500/'+data["poster_path"]
    return poster_url
    

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[1:6]

    recommended_movies=[]
    recommend_movies_posters=[]
    
    for i in movie_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_posters(movie_id))
    return recommended_movies,recommend_movies_posters

selected_movie=st.selectbox('How are you?',movies['title'].values)

if st.button('Recommend'):
    recommended_movies, recommend_movies_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movies[0])
        
        st.image(recommend_movies_posters[0])

    with col2:
        st.text(recommended_movies[1])
        
        st.image(recommend_movies_posters[1])

    with col3:
        st.text(recommended_movies[2])
        
        st.image(recommend_movies_posters[2])

    with col4:
        st.text(recommended_movies[3])
        
        st.image(recommend_movies_posters[3])

    with col5:
        st.text(recommended_movies[4])
        
        st.image(recommend_movies_posters[4])







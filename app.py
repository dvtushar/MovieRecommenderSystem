import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
movies_list = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'which movie do you wanna watch?',
    movies_list
)
if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])

    st.markdown("<div style='margin-left: 20px; margin-right: 20px;'></div>",
                unsafe_allow_html=True)  # Adjust the margin as needed

    with col2:
        st.text(name[1])
        st.image(posters[1])

    st.markdown("<div style='margin-left: 20px; margin-right: 20px;'></div>",
                unsafe_allow_html=True)

    with col3:
        st.text(name[2])
        st.image(posters[2])

    st.markdown("<div style='margin-left: 20px; margin-right: 20px;'></div>",
                unsafe_allow_html=True)

    with col4:
        st.text(name[3])
        st.image(posters[3])

    st.markdown("<div style='margin-left: 20px; margin-right: 20px;'></div>",
                unsafe_allow_html=True)

    with col5:
        st.text(name[4])
        st.image(posters[4])

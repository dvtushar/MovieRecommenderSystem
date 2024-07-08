# Movie Recommender System

Welcome to the **Movie Recommender System** GitHub repository! This project leverages machine learning techniques to provide personalized movie recommendations. The web application is built using Chainlit and Streamlit, offering an interactive and user-friendly interface.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The **Movie Recommender System** aims to enhance the movie-watching experience by suggesting movies that users are likely to enjoy based on their past ratings and preferences. The system is built using a machine learning model trained on a dataset of over 5000 movies and reviews.

## Features

- **Personalized Recommendations**: Get movie suggestions tailored to your tastes.
- **Interactive Web Application**: Use Chainlit and Streamlit for a seamless user experience.
- **Comprehensive Dataset**: Trained on a dataset of more than 5000 movies and reviews.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dvtushar/MovieRecommenderSystem.git
   cd MovieRecommenderSystem

2. **Create a Virtual Environment**
    python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. **Install Dependencies**
   pip install -r requirements.txt

## Usage
1. **Run the Web Application**
   ```bash
   streamlit run app.py
2. **Access the Application**
   Open your browser and go to http://localhost:8501 to use the Movie Recommender System.

## Model Training 
The machine learning model is trained using collaborative filtering techniques on a dataset of more than 5000 movies and their reviews. The training process includes:

- **Data Preprocessing**: Cleaning and preparing the data for model training.
- **Model Selection**: Choosing the appropriate machine learning algorithms.
- **Training**: Training the model using the preprocessed data.
- **Evaluation**: Assessing the model's performance and making necessary adjustments.

## Dataset
The dataset used in this project comprises over 5000 movies and reviews. It includes information such as movie titles, genres, ratings, and user reviews.

## Contributing

We welcome contributions to enhance the Movie Recommender System. If you would like to contribute, please follow these steps:

1. **Fork** the repository on GitHub.
2. **Clone** the forked repository to your local machine.
   ```bash
   git clone https://github.com/dvtushar/MovieRecommenderSystem.git
   cd MovieRecommenderSystem
3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeature

4. **Commit Your Changes**
   ```bash
   git commit -m 'Add some feature'
5. **Push to the Branch**
   git push origin feature/YourFeature

## Contact
- **Author**: Tushar Dev
- **Email**: tushardev.work@gmail.com
- **GitHub**: dvtushar
Thank you for checking out the Movie Recommender System! We hope you find it useful and enjoyable.
PS: As the original size of the similarity.pkl file was exceeding 100mb find it on the following drive link: "https://drive.google.com/file/d/1oer00Z6X4vs_LGOolio1bHthv47UO3J6/view?usp=sharing"

   


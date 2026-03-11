# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using **Python, Natural Language Processing (NLP), and Machine Learning**.  
The system recommends movies similar to the selected movie using **Cosine Similarity**.

---

## 🚀 Features
- Content-based movie recommendation
- NLP-based feature extraction
- Bag of Words using CountVectorizer
- Similarity calculation using Cosine Similarity
- Recommends Top 5 similar movies
- Interactive Streamlit Web Application

---

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- NLP (CountVectorizer)
- Streamlit

---

## 📂 Project Structure

```
movie-recommendation-system
│
├── recommend.py
├── Movie_Recommended.ipynb
├── movies.pkl
├── README.md
└── dataset
    └── tmdb_movies.csv
```

---

## 📊 How It Works

1. Data preprocessing and cleaning
2. Feature engineering
3. Convert text features into vectors using Bag of Words
4. Calculate similarity between movies using Cosine Similarity
5. Recommend movies based on highest similarity scores

---

## 💻 Run Locally

Clone the repository

```bash
git clone https://github.com/1206-Anuj/movie-recommendation-system.git
```

Go to the project directory

```bash
cd movie-recommendation-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📸 Application Demo

Select a movie from the dropdown and the system will recommend **5 similar movies instantly**.

---




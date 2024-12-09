import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

def load_and_preprocess_data(csv_file_path="C:\\Users\\7300\\Downloads\\AI project\\movie_data_large.csv"):
    try:
        df = pd.read_csv(csv_file_path)
        
        print(f"Dataset loaded: {df.shape[0]} rows and {df.shape[1]} columns.")
        print(df.head())  

        if 'Movie Title' not in df.columns or 'Lead Actor' not in df.columns:
            raise ValueError("Missing required columns: 'Movie Title' or 'Lead Actor'")

        df.dropna(inplace=True)

        return df
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
        raise
    except ValueError as ve:
        print(f"Error: {ve}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def train_model(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['Movie Title'])
    y = df['Lead Actor']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000)
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    return model, vectorizer

def save_model_and_vectorizer(model, vectorizer, model_filename='movie_predictor_model.pkl', vectorizer_filename='vectorizer.pkl'):
    joblib.dump(model, model_filename)
    joblib.dump(vectorizer, vectorizer_filename)
    print(f"Model and vectorizer saved as {model_filename} and {vectorizer_filename}.")

def predict_movie_lead_actor(movie_title, model, vectorizer):
    title_vector = vectorizer.transform([movie_title])
    predicted_actor = model.predict(title_vector)[0]
    return predicted_actor

def main():
    csv_file_path = r"C:\Users\7300\Downloads\AI project\movie_data_large.csv"

    df = load_and_preprocess_data(csv_file_path)

    model, vectorizer = train_model(df)

    save_model_and_vectorizer(model, vectorizer)

    movie_title = "Inception"
    predicted_actor = predict_movie_lead_actor(movie_title, model, vectorizer)
    print(f"The predicted lead actor for '{movie_title}' is {predicted_actor}.")

if __name__ == '__main__':
    main()

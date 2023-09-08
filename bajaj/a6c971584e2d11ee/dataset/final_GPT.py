import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')

train_data = pd.read_csv("train.csv")

def preprocess_text(text):
    text = text.lower()
    
    words = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)
train_data['text_cleaned'] = train_data['text'].apply(preprocess_text)

X = train_data['text_cleaned']
y = train_data['cls']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_val_tfidf = vectorizer.transform(X_val)

classifier = MultinomialNB()
classifier.fit(X_train_tfidf, y_train)

y_pred = classifier.predict(X_val_tfidf)
accuracy = accuracy_score(y_val, y_pred)
print("Validation Accuracy:", accuracy)
print(classification_report(y_val, y_pred))

test_data = pd.read_csv("test.csv")
test_data['text_cleaned'] = test_data['text'].apply(preprocess_text)
X_test = test_data['text_cleaned']

X_test_tfidf = vectorizer.transform(X_test)

test_predictions = classifier.predict(X_test_tfidf)

submission_df = pd.DataFrame({'ID': test_data['ID'], 'cls': test_predictions})
submission_df.to_csv("submission.csv", index=False)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Ініціалізація інструментів
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

# Читання тексту
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Токенізація
tokens = word_tokenize(text)

# Видалення пунктуації
tokens = [word for word in tokens if word not in string.punctuation]

# Видалення стоп-слів
tokens = [word for word in tokens if word.lower() not in stop_words]

# Лемматизація та стеммінг
processed_tokens = [lemmatizer.lemmatize(stemmer.stem(word.lower())) for word in tokens]

# Запис результатів
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(processed_tokens))

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Завантажити ресурси NLTK
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Читання тексту з файлу
with open('edgeworth-parents.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Токенізація тексту
tokens = word_tokenize(text.lower())  # Зниження регістру для уніфікації

# Визначення кількості слів
word_count = len(tokens)
print(f"Загальна кількість слів у тексті: {word_count}")

# Частоти слів без очищення
word_freq = Counter(tokens)
most_common_words = word_freq.most_common(10)

# Побудова графіка найвживаніших слів
plt.bar(*zip(*most_common_words))
plt.title("10 найбільш вживаних слів (без очищення)")
plt.xticks(rotation=45)
plt.show()

# Видалення стоп-слів і пунктуації
stop_words = set(stopwords.words('english'))
cleaned_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

# Частоти очищених слів
cleaned_word_freq = Counter(cleaned_tokens)
most_common_cleaned_words = cleaned_word_freq.most_common(10)

# Побудова графіка найвживаніших слів після очищення
plt.bar(*zip(*most_common_cleaned_words))
plt.title("10 найбільш вживаних слів (після очищення)")
plt.xticks(rotation=45)
plt.show()
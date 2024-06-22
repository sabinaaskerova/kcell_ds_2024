import re
from collections import Counter


# Если все слова встречаются один раз, то возвращается первое слово в тексте
def analyze_text(text):
    # Clean and tokenize the text
    words = re.findall(r'\w+', text.lower())

    if not words:
        return "Empty text."

    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]

    longest_word = max(words, key=len)

    return most_common_word, longest_word

text = "Python is an amazing language. It is widely used in data science and web development."
most_common, longest = analyze_text(text)
print("Наиболее часто встречающееся слово:", most_common)
print("Самое длинное слово:", longest)
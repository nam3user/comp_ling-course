import re
import nltk
import spacy

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        pass

# Реализация простой токенизации

    def simple_tokenize(self, text) -> list[str]:
        if not isinstance(text, str):
          raise TypeError("Текст должеен быть в str")
        else:
          tokens = re.findall(r"\w+", text)
          return tokens

# Реализация NLTK токенизации

    def nltk_tokenize(self, text)  -> list[str]:
        nltk.download('punkt')
        nltk.download('punkt_tab')
        from nltk.tokenize import word_tokenize, sent_tokenize
        if not isinstance(text, str):
          raise TypeError("Текст должен быть в str")
        else:
          which = input('For NLTK: Tokenize by word or sentence? Pick 1 or 2. ')
          while which != "1" and which != "2":
            print('Invalid')
            which = input('For NLTK: Tokenize by word or sentence? Pick 1 or 2. ')
          if which == "1":
            return word_tokenize(text)
          else:
            return sent_tokenize(text)

 # Реализация spaCy токенизации

    def spacy_tokenize(self, text) -> list[str]:
        if not isinstance(text, str):
          raise TypeError("Текст должеен быть в str")
        else:
          nlp = spacy.load("en_core_web_sm")
          doc = nlp(text)
          return [t.text for t in doc]

# Реализация вызова всех методов

    def tokenize_all(self, text):
        all_met = {
            "simple tokenizing" : self.simple_tokenize(text), 
            'nltk tokenizing' : self.nltk_tokenize(text), 
            'spacy tokenizing' : self.spacy_tokenize(text)}
        return all_met

# Пример использования

def demo():
    tokenizer = TextTokenizer()
    sample_text = "Hello, world! This is a test sentence. How are you today?"
    results = tokenizer.tokenize_all(sample_text)
    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    demo()
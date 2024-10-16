from bs4 import BeautifulSoup
from googletrans import Translator
import requests

translator = Translator()


def get_english_words():
    url = 'https://randomword.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    english_word = soup.find("div", id="random_word").text.strip()  # Слово на английском
    word_definition = soup.find("div", id="random_word_definition").text.strip()  # Определение слова

    return {
        "english_word": english_word,
        "word_definition": word_definition
    }

def word_game():
    print("Добро пожаловать в игру")

    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_word")
        word_definition = word_dict.get("word_definition")

        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        print(f"Значение слова - {translated_definition}")

        user = input("Что это за слово? ")

        if user.lower() == translated_word.lower():
            print("Ответ правильный!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        play_again = input("Хотите сыграть еще раз? (y/n): ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


word_game()



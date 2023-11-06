
from transformers import pipeline

translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")

print(translator("Я все же надеюсь сдать эту сессию ")[0]['translation_text'])

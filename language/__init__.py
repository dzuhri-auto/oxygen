# import language dicts from which ever folder and file they are,
# e.g i have id.py so i import it here
from language.id import id
from language.en import en

supported_lang = [
    {"name": "English", "symbol": "en", "dict": en},
    {"name": "Indonesia", "symbol": "id", "dict": id},
]

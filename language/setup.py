def process_language():
    from types import SimpleNamespace
    from language import supported_lang

    class NestedNamespace(SimpleNamespace):
        def __init__(self, dictionary, **kwargs):
            super().__init__(**kwargs)
            for key, value in dictionary.items():
                if isinstance(value, dict):
                    self.__setattr__(key, NestedNamespace(value))
                else:
                    self.__setattr__(key, value)

    lang_text = {}
    for dict_lang in supported_lang:
        lang_text.update({dict_lang.get("symbol"): NestedNamespace(dict_lang.get("dict"))})
    return lang_text

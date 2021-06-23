'''translator'''
import json
from ibm_watson import LanguageTranslatorV3, language_translator_v3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# def translate(str, locale_id):
#     return language_translator.translate(
#     text= str,
#     model_id=locale_id).get_result()

# def json_translation_to_str(json):
#     return json['translations'][0]['translation']

# def translation_lang_id(text_lang, desired_lang):
#     return f'{text_lang}-{desired_lang}' 

# authenticator = IAMAuthenticator('sbhcOFiS81fKkMZkdb_GnEhckGFkpKJC0aBSdl7NmXqF')
# language_translator = LanguageTranslatorV3(
#     version = '2018-05-01',
#     authenticator = authenticator
# )
# URL_WATSON = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b4d58194-df13-4160-9a74-ede7fde5dab2'
# language_translator.set_service_url(URL_WATSON)
# languages = language_translator.list_identifiable_languages().get_result()

# text_to_translate = input("Enter text to translate:")
# text_language = language_translator.identify(text_to_translate).get_result()['languages'][0]['language']


# print(
#     json_translation_to_str(
#         translate(text_to_translate, translation_lang_id(text_language, 'fr'))
#     )
# )

# def english_to_french(str):
#     if not str:
#         translation = "Nothing to translate"
#     else:
#         translation = json_translation_to_str(translate(str, translation_lang_id('en', 'fr')))
#     return translation


config = { 
    'watson_url': 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b4d58194-df13-4160-9a74-ede7fde5dab2',
    'authenticator': 'sbhcOFiS81fKkMZkdb_GnEhckGFkpKJC0aBSdl7NmXqF',
    'version': '2018-05-01'
    }

class MyTranslator:
    
    def configure(conf):
        language_translator = LanguageTranslatorV3(
        version = conf['version'],
        authenticator = IAMAuthenticator(conf['authenticator'])
        )
        language_translator.set_service_url(conf['watson_url']) 
        return language_translator 

class TranslationProc:
    def __init__(self, str) -> None:
        self.translator = MyTranslator.configure(config)
        self.str = str

    def translate_user_prompt(self):
        def define_lang():
            return self.translator.identify(self.str).get_result()['languages'][0]['language']

        def translate(locale_id):
            return self.translator.translate(
                text = self.str,
                model_id=locale_id).get_result()
        
        def json_translation_to_str(json):
            return json['translations'][0]['translation']

        def translation_lang_id(text_lang, desired_lang):
            return f'{text_lang}-{desired_lang}'

        if not self.str:
            translation = "Nothing to translate"
        else:
            translation = json_translation_to_str(translate(translation_lang_id(define_lang(), 'fr')))
        return translation

abc =TranslationProc("Some shit").translate_user_prompt()
print(abc)
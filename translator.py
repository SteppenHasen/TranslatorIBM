'''translator'''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def translate(str, locale_id):
    return language_translator.translate(
    text= str,
    model_id=locale_id).get_result()

def json_translation_to_str(json):
    return json['translations'][0]['translation']

def translation_lang_id(text_lang, desired_lang):
    return f'{text_lang}-{desired_lang}' 

authenticator = IAMAuthenticator('sbhcOFiS81fKkMZkdb_GnEhckGFkpKJC0aBSdl7NmXqF')
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
URL_WATSON = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/b4d58194-df13-4160-9a74-ede7fde5dab2'
language_translator.set_service_url(URL_WATSON)
# languages = language_translator.list_identifiable_languages().get_result()

# text_to_translate = input("Enter text to translate:")
# text_language = language_translator.identify(text_to_translate).get_result()['languages'][0]['language']


# print(
#     json_translation_to_str(
#         translate(text_to_translate, translation_lang_id(text_language, 'fr'))
#     )
# )



# config = { watson_url: 'sdf', authenticator: 'sdfssdfs', skdjfkdjf }
# translator = Translater.configure(config)
# translator.translate_user_prompt()

def english_to_german(str):
    if not str:
        translation = "Nothing to translate"
    else:
        translation = json_translation_to_str(translate(str, translation_lang_id('en', 'de')))
    return translation

def english_to_french(str):
    if not str:
        translation = "Nothing to translate"
    else:
        translation = json_translation_to_str(translate(str, translation_lang_id('en', 'fr')))
    return translation
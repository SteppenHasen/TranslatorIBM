'''translator'''
import json
from ibm_watson import LanguageTranslatorV3, language_translator_v3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import dotenv_values
import inquirer

config = dotenv_values(".env")
question = [
  inquirer.List('lang',
                message="What language do you need?",
                choices=['en', 'fr', 'de', 'af', 'uk', 'ja'],
            ),
]
answer = inquirer.prompt(question)

class TranslationProc:
    def __init__(self, str) -> None:
        self.translator = TranslationProc.configure(config)
        self.str = str

    def configure(conf):
        language_translator = LanguageTranslatorV3(
        version = conf['VERSION'],
        authenticator = IAMAuthenticator(conf['AUTHENTICATOR'])
        )
        language_translator.set_service_url(conf['WATSON_URL']) 
        return language_translator 

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
            translation = json_translation_to_str(translate(translation_lang_id(define_lang(), answer['lang'])))
        return translation

TranslationProc.configure(config)
print(TranslationProc("Some awesome code").translate_user_prompt())
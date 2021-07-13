from django.db import models
# from translate.apps import Translanor
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import dotenv_values

# config = dotenv_values(".env")
# translation_engine = LanguageTranslatorV3(
#     version = config['VERSION'],
#     authenticator = IAMAuthenticator(config['AUTHENTICATOR'])
# )
# translation_engine.set_service_url(config['WATSON_URL'])
# print(Translator.call(translation_engine, "Some", answer['lang']))

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Translation(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    translated_text = models.TextField()

    EMPTY_STRING = "Nothing to translate"

    @staticmethod
    def call(translation_engine, string, lang):
        return Translation(translation_engine, string, lang).instance_call()

    def __init__(self, translation_engine, string, lang) -> None:
        self.translation_engine = translation_engine
        self.string = string
        self.desired_lang = lang

    def instance_call(self):
        return self.EMPTY_STRING if not self.string else self.__translate__()

    def __translate__(self):
        return self.__json_translation_to_str__(
                self.__call_translation_api__()
            )

    def __json_translation_to_str__(self, json):
        return json['translations'][0]['translation']

    def __call_translation_api__(self):
        return self.translation_engine.translate(text = self.string, model_id = self.__lang_id()).get_result()

    def __base_lang__(self):
        return self.translation_engine.identify(self.string).get_result()['languages'][0]['language']

    def __lang_id(self):
        return f'{self.__base_lang__()}-{self.desired_lang}'

    def __str__(self):
        return self.translated_text
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version= '2022-07-05'


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    '''This Method translates English to French'''
    model_id = 'en-fr'
    french_text = language_translator.translate(
    text=english_text,
    model_id=model_id ).get_result()['translations'][0]['translation']
    #print(frenchText)
    return french_text

def french_to_english(french_text):
    '''This Method translates French to English'''
    model_id = 'fr-en'
    english_text = language_translator.translate(
    text=french_text,
    model_id=model_id ).get_result()['translations'][0]['translation']
    #print(englishText)
    return english_text
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2018-05-01'


authenticator = IAMAuthenticator('ih32Mpf7HBORYkJW5hjWnN3-fLeaKWRvya8sScR1NnPh')
language_translator = LanguageTranslatorV3(
    version=VERSION, authenticator=authenticator)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/13796a83-0983-4a5e-85c6-c906c684c33e')


def english_to_french(english_text):
    response = language_translator.translate(
        text=english_text, model_id='en-fr').get_result()
    french_text = response['translations'][0]['translation']

    return french_text
    
def french_to_english(french_text):
    response = language_translator.translate(
        text=french_text, model_id='fr-en').get_result()
    english_text = response['translations'][0]['translation']

    return english_text

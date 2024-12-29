# Azure Translation
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
import os

azureKeyCredential = AzureKeyCredential(os.getenv("AZURE_TRANSLATE_API_KEY"))
textTranslationClient = TextTranslationClient(
    credential=azureKeyCredential,
    endpoint=os.getenv("AZURE_TRANSLATE_API_ENDPOINT"),
    region=os.getenv("AZURE_TRANSLATE_API_REGION")
)

def azure_translate(user_input: list, to_language: list):
    try:
        response = textTranslationClient.translate(body=user_input, to_language=to_language)
        translations = response if response else None

        if translations:
            result = ''
            for translation in translations:
                detected_language = translation.detected_language
                if detected_language:
                    print(f"Detected languages of the input text: {detected_language.language} with score: {detected_language.score}.")
                for translated_text in translation.translations:
                    result += f"翻譯出的語言是:'{translated_text.to}'\n翻譯出的結果: '{translated_text.text}'\n"
            return result
    except HttpResponseError as exception:
        if exception.error is not None:
            print(f"Error Code: {exception.error.code}")
            print(f"Message: {exception.error.message}")

result = azure_translate(["Hello", "World"], ["zh-Hant", "ja"])
print('================================================')
print(result)
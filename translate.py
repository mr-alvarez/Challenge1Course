from dotenv import load_dotenv
import os

# import namespaces
import azure ## changes included by camilo to test azure sdk v2.0.0



def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        translatorRegion = os.getenv('TRANSLATOR_REGION')
        translatorKey = os.getenv('TRANSLATOR_KEY')

        # Create client using endpoint and key
        azure.add_credentials(translatorRegion, translatorKey) #changes included by camilo to test github 


        ## Choose target language
        sourceLanguage = "en"  
        targetLanguage = "es"   



        # Translate text



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
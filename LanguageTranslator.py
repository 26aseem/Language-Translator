#Code for Language Translation using IBM Watson Language Translator Version  API

from ibm_watson import LanguageTranslatorV3
import pandas as pd

#Credentials
apiKey = "xQBJf0D6NiKMG-M_beEUke1cuCldf4m5Sxjk-aAPlu4i"
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/4557665d-75f1-41b5-90c5-20ab8d4b2d1c"
version = "2018-05-01"

#Instance is created
langTrans = LanguageTranslatorV3(iam_apikey = apiKey,url = url,version = version)

#Languages selection
print("Choose the from-to LANGUAGE pair\n")

#List of Language code
df = pd.DataFrame(langTrans.list_identifiable_languages().get_result())
for i in range(0,len(df),1):
    print("Type " + df.iloc[i,0]['language'] + " for " + df.iloc[i,0]['name'] + "\n" )

#Enter the language codes from the list
From = input("Enter the first Language\n")
To = input("Enter the second Language\n")
From2To = From + "-" + To

# Text to be translated is read from the file
file = open("transText.txt","r")
transText = file.read()

#API request is sent
TransRequest = langTrans.translate(text = transText, model_id = From2To)
getResult = TransRequest.get_result()
Result = getResult['translations'][0]['translation']
print(Result)

#Result is printed

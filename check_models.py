from google import genai

client = genai.Client(api_key="AIzaSyAbYVj2lm1wV7YBDhcBslQXMxx0cPlfLgo")

for model in client.models.list():
    print(model.name)
mport requests

def translate(word):
    url = "https://dictionary.cambridge.org/api/v1/dictionaries/english-vietnamese/search?q=" + word
    response = requests.get(url)
    data = response.json()
    try:
        definition = data["results"][0]["meanings"][0]["definition"]
        example = data["results"][0]["meanings"][0]["examples"][0]["text"]
        return definition, example
    except:
        return "No definition found for the given word."
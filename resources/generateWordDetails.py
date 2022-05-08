from bs4 import BeautifulSoup
import requests 

class WordOfTheDay:
    def get_word_of_the_day_details():
        try:
            word_of_the_day_url = 'https://www.merriam-webster.com/word-of-the-day'
            page = requests.get(word_of_the_day_url)
            soup = BeautifulSoup(page.content, "html.parser")
            name = soup.find(class_= 'word-and-pronunciation').h1
            wordOfTheDay = name.text.strip()
            get_descriptions = soup.find(class_= 'wod-definition-container')
            data = get_descriptions.find_all('p')
            descriptions = data[0].get_text()
            usage = data[1].get_text()
            result ="Success"     
        except Exception as e:
            print(e.message)
            result ="Failed"
        context ={"result" : result, 'word' : wordOfTheDay, 'description': descriptions, 'usage' : usage}
        return context

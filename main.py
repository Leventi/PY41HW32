import requests

WIKIURL = 'https://en.wikipedia.org/wiki/'

class WikiLinks:

    URL = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'

    def get_country(self, country_id):
        response = requests.get(self.URL)
        res_data = response.json()
        return res_data[country_id]['name']['common']

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        country = self.get_country(self.cursor)
        if country is None:
            raise StopIteration
        return country


with open('wikilinks.txt', 'w', encoding='utf-8') as f:
    for country in WikiLinks():
        country_str = country + ' - ' + WIKIURL + country.replace(" ", "_")
        f.write(country_str + '\n')

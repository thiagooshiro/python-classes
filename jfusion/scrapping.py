import requests
from bs4 import BeautifulSoup
import json

# URL da página inicial que queremos fazer o scraping
base_url = 'http://quotes.toscrape.com/page/{}/'

# Função para raspar citações de várias páginas
def scrape_quotes(num_pages):
    all_quotes = []
    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        response = requests.get(url)
        
        if response.status_code != 200:
            continue
        
        soup = BeautifulSoup(response.content, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            all_quotes.append({
                'text': text,
                'author': author
            })
        
        # Parar quando tivermos pelo menos 10 citações
        if len(all_quotes) >= 10:
            break
    
    return all_quotes[:10]  # Retornar exatamente 10 citações

# Coletar 10 citações aleatórias
quotes_to_save = scrape_quotes(5)  # Exemplo: coletar de 5 páginas

# Salvar as citações em um arquivo JSON
with open('quotes.json', 'w', encoding='utf-8') as json_file:
    json.dump(quotes_to_save, json_file, ensure_ascii=False, indent=4)

print(f'Dados salvos em quotes.json, total de citações coletadas: {len(quotes_to_save)}')

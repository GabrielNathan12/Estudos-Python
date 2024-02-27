import requests
import re
from bs4 import BeautifulSoup
#python -m http.server -d .\intermediario\aulas_curso_1\web\1\aula_site\ 3333
url = 'http://localhost:3333/'
response = requests.get(url)

raw_html = response.text

parse_html = BeautifulSoup(raw_html,'html.parser', from_encoding='utf-8')
#print(raw_html)
print(parse_html.title.text)

top_jobs = parse_html.select_one('#intro > div > div > article > h2')

print(top_jobs.text)

article = top_jobs.parent

#print(article)

for p in article.select('p'):
    print(re.sub(r'\s{1,}', ' ', p.text).strip())
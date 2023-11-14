#librerias beautifulsoup, requests
import bs4
import requests 

resultado_busqueda = requests.get('https://escueladirecta-blog.blogspot.com/2023/05/configurando-la-impresion-perfecta-de.html')

print(resultado_busqueda.text)
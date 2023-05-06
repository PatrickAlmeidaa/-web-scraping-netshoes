import requests
from bs4 import BeautifulSoup
from PIL import Image
from fpdf import FPDF

def requisicaoSite(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    html = response.text
    return html

def criaPDF(title, price, description, attributes, img):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", "B", 16)
    pdf.cell(txt= title, w = 0, align="c")

    pdf.ln(8.0)
    pdf.set_font("Times", "", 14)
    pdf.cell(txt= "Criado por Patrick Araújo de Almieda", w = 0, align="c")

    pdf.ln(10.0)
    pdf.set_font("Times", "", 14)
    pdf.multi_cell(txt= description, w = 0, align="j")

    pdf.ln(5.0)
    pdf.multi_cell(txt= attributes, w = 0, align="j")
    
    pdf.ln(5.0)
    pdf.set_font("Times", "B", 16)
    pdf.multi_cell(txt= price, w = 0, align="c")

    pdf.ln(5.0)
    pdf.image(img)
    
    pdf.output("dados_produto.pdf")

class ProductScraper:
    def scrape(self, url):
        html = requisicaoSite(url)
        soup = BeautifulSoup(html, 'html.parser')

        # extrair informações do produto
        div = soup.find('div', class_='short-showcase-description')
        section = div.find('section', class_='short-description')
        title = section.find('h1', attrs={'data-productname': True}).text.strip()

        price = soup.find('div', {'class': 'default-price'}).text.strip()

        description = soup.find('p', {'itemprop': 'description'}).text.strip()

        info = {}
        attributes = soup.find('ul', {'class': 'attributes'}).text.strip()
        attributes = BeautifulSoup(str(attributes), 'html.parser')
        for attribute in attributes.find_all('li'):
            key = attribute.find('strong').text.strip()
            value = attribute.text.replace(key, '').strip()
            value = value + '\n'
            info[key] = value   
    
        # baixar imagem do produtocute punch
        img_url = soup.find('img', {'class': 'zoom'})['src']
        img_data = requests.get(img_url).content
        with open('product.jpg', 'wb') as f:
            f.write(img_data)

        # exibir informações do produto
        #print(f'Título: {title}')
        #print(f'Preço: {price}')
        #print(f'Descrição: {description}')
        #print(f"Atributos: {attributes}")
        img = Image.open('product.jpg')
        img.show()

        criaPDF(title, price, description, attributes, img)


scraper = ProductScraper()
scraper.scrape('https://www.netshoes.com.br/bone-adidas-aba-curva-snapback-daily-logo-linear-preto+branco-FB8-3589-026')


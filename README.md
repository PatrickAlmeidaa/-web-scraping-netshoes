# Web Scraping de Produto da Netshoes
Este é um projeto de web scraping para coletar informações sobre produtos da Netshoes, como nome, preço, descrição, atributos e imagem. O objetivo é extrair informações úteis para análises de mercado, pesquisa de preços e comparação de produtos.

## Como funciona
O projeto é desenvolvido em Python, utilizando a biblioteca beautifulsoup4 para fazer a coleta de dados do HTML da página do produto selecionado, e a biblioteca fpdf2 para gerar um PDF com as informações coletadas.

Para executar o projeto, siga os passos abaixo:
1. instale as dependencias da biblioteca beautifulsoup4
```Bash
pip install beautifulsoup4
```
2. instale as dependencias da biblioteca requests
```Bash
pip install requests
```
3. instale as dependencias da biblioteca Pillow
```Bash
pip install Pillow
```
4. instale as dependencias da biblioteca fpdf2
```Bash
pip install fpdf2
```
5. execute o código
```Bash
python3 coleta_dados_netshoes.py
```
O script solicitará o link do produto a ser utilizado. Copie o link do produto na página da Netshoes, abra o scripto no editor de texto e cole no código como no exemplo a baixo. O script irá extrair as informações do produto e gerar um arquivo PDF com as informações coletadas.

```Python
scraper.scrape('produto_netshoes_desejado')
```
## Importante
Os dados coletados do produto desejado estárão disponiveis no PDF nomeado como "dados_produto.pdf" para facilitar a visualização. 

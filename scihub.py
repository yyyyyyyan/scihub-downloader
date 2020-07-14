from bs4 import BeautifulSoup
import requests

SCIHUB_DOMAIN = "https://sci-hub.tw"

def download_article(search_str, download_to):
    response = requests.post(SCIHUB_DOMAIN, data={"request": search_str})   # Manda um post passando a string de pesquisa (URL/DOI/Nome)
    if response.status_code == 200 and response.history:                    # Checa se a requisição foi bem sucedida (200) e se houve redirecionamento
        soup = BeautifulSoup(response.content, "lxml")
        pdf_url = "https:" + soup.find("iframe", id="pdf")["src"]           # URL no iFrame começa com //<dominio>, por isso adiciona "https:" antes
        pdf = requests.get(pdf_url)
        if pdf.status_code == 200:
            with open(download_to, "wb") as pdf_file:
                pdf_file.write(pdf.content)
            return True
    return False
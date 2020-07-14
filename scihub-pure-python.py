from urllib.request import Request, urlopen
from urllib.parse import urlencode
import re

SCIHUB_DOMAIN = "https://sci-hub.tw"

def download_article(search_str, download_to):
    data = urlencode({"request": search_str}).encode("utf8")
    req = Request(SCIHUB_DOMAIN, data)
    response = urlopen(req)                                                 # Manda um post passando a string de pesquisa (URL/DOI/Nome)
    if response.status == 200 and response.geturl() != SCIHUB_DOMAIN:       # Checa se a requisição foi bem sucedida (200) e se houve redirecionamento
        html = response.read().decode("utf8")
        iframe = re.search(r'<iframe src = "(.*)" id = "pdf"', html)
        pdf_url = "https:" + iframe.group(1)                            # URL no iFrame começa com //<dominio>, por isso adiciona "https:" antes
        pdf = urlopen(pdf_url)
        if pdf.status == 200:
            with open(download_to, "wb") as pdf_file:
                pdf_file.write(pdf.read())
            return True
    return False
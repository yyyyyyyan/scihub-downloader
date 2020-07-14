# scihub-downloader
Exemplo rápido de como baixar PDFs do SciHub

O [scihub.py](https://github.com/yyyyyyyan/scihub-downloader/blob/master/scihub.py) requer a instalação dos pacotes `requests`, `beautifulsoup4` e `lxml` (esse último é frescura), todos disponíveis no PyPI.

O [scihub-pure-python.py](https://github.com/yyyyyyyan/scihub-downloader/blob/master/scihub-pure-python.py) roda em Python puro, sem instalações extras.

Pra ambos, a chamada seria:

```python
>>> download_article("https://doi.org/10.1016/j.biopha.2020.110230", "artigos/artigo1.pdf")
True
>>> download_article("Advances in the relationship between coronavirus infection and cardiovascular diseases", "artigos/artigo2.pdf")
True
>>> download_article("esse artigo não existe", "artigos/artigo3.pdf")
False
>>> import os
>>> os.listdir("artigos")
['artigo1.pdf', 'artigo2.pdf']
```

Isso é só um exemplo e deve ser ajustado.

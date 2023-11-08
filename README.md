# Web Scraping da Captura de preços (Drogaria)

  

Este é um projeto de web scraping para extrair dados do site da Drogasil. Ele permite coletar informações relevantes do site (como Nome, EAN, Preço, etc..) da Drogasil e armazená-las em um arquivo CSV para análise posterior.

  

## Requisitos

  

Antes de iniciar, certifique-se de ter os seguintes requisitos:

  

1. Python instalado: Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

  

2. Bibliotecas dependentes: Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`. Você pode fazer isso abrindo o terminal (prompt de comandos ou CMD) e executar o seguinte comando no terminal:

  
```bash
pip install -r requirements.txt
```

  
  

## Como Usar

  

Siga os passos abaixo para utilizar o script:

  

1. Navegue até a pasta raiz do projeto.

  

2. Execute o script com o seguinte comando:

  
```bash
scrapy crawl drogasil -o arquivo.csv
```

Substitua `arquivo.csv` pelo nome que deseja atribuir ao arquivo de saída, onde os dados coletados serão armazenados no formato CSV.

  

## Resultados

  

O arquivo CSV gerado será salvo dentro do diretório do projeto, e você poderá usá-lo para análise.



---
© 2023, Natan.
import scrapy
import re

class DrogasilSpider(scrapy.Spider):
    name = "drogasil"
    start_urls = ["https://www.drogasil.com.br/categorias"]

    def parse(self, response):
        # Extrai todas as categorias para navegar em seus produtos
        categorias = response.xpath('//h3')
        for categoria in categorias:
            # Tratamento de String
            if not 'GAM' in str(categoria.xpath('string()').get()):
                if not 'GROWTH' in str(categoria.xpath('string()').get()):
                    # Grava o nome da categoria e o link de acesso à página
                    nome_categoria = categoria.xpath('string()').get()
                    link = categoria.xpath('.//a/@href').get()
                    yield scrapy.Request(url=link, callback=self.parse_categoria, meta={'nome_categoria': nome_categoria})

    def parse_categoria(self, response):
        nome_categoria = response.meta['nome_categoria']
        # Percorre todos os produtos da categoria
        sessao_produtos = response.xpath('//section')
        for section in sessao_produtos:
            tag_a = section.xpath('./following-sibling::a')
            for a in tag_a:
                link = a.xpath('@href').get()
                # Vai para os detalhes do produto
                yield scrapy.Request(url=link, callback=self.parse_produto, meta={'nome_categoria': nome_categoria})

    def parse_produto(self, response):
        # Salva e retorna os detalhes dos produtos
        nome = response.xpath('//h1/text()').get().strip()
        preco = 'R$' + response.xpath('//span[text()="R$"]/../text()').get()
        ean = response.xpath('//th[text()="EAN"]/following-sibling::td//text()').get().strip()
        descricao = re.sub(r'<.*?>', ' ', response.xpath('//h2[text()="Descrição do Produto"]/following-sibling::div').get()).replace('\xa0', '').strip()
        nome_categoria = response.meta['nome_categoria']
        yield {
            'nome': nome,
            'preco': preco,
            'ean': ean,
            'categoria': nome_categoria,
            'descricao': descricao,
        }

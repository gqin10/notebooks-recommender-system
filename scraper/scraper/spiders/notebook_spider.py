import scrapy


class NotebookSpider(scrapy.Spider):
    name = 'notebook_spider'
    allowed_domains = ['harveynorman.com.my']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(NotebookSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get("url")]

    def parse(self, response):
        # get links of each product page
        product_names = response.xpath("//div[@class='product-info']/a/@href").getall()

        # parse each collected page
        for n in product_names:
            yield response.follow(url=n, callback=self.parse_item_page)

        # get the link of next page from pager
        next_page = response.xpath(
            "//div[@class='pagination-wrap col-xs-12 pagination-bottom cm-pagination-wraper']/ol[@class='pager pager-inline']/li/a[@class='next cm-history cm-ajax']/@href").get()

        # parse next page if exist
        if (next_page != None):
            yield response.follow(url=next_page, callback=self.parse)

    def parse_item_page(self, response):
        values = {}  # a dictionary to store item's properties

        item_name = response.xpath("//h1[@class='fn product-title']/text()").extract()
        price = response.xpath("//span[@class='price']/span[@class='price-num']/text()").extract()

        features = response.xpath("//table/tbody/tr")
        for f in features:
            name = f.xpath("./th/strong/text()").get()
            if name:
                val = f.xpath("./td/text()").get()
                # store properties and their corresponding values into the dictionary
                values[name] = val

        values["Price (RM)"] = price[1].replace(",", "").strip()

        yield values

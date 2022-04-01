import scrapy


class NotebookCheckSpider(scrapy.Spider):
    name = 'notebook_check_spider'
    allowed_domains = ['notebookcheck.net']
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(NotebookCheckSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get("url")]

    def parse(self, response):
        item1 = response.xpath("//table/tr[contains(@class,'odd')]")
        item2 = response.xpath("//table/tr[contains(@class,'even')]")
        items = item1 + item2

        for item in items:
            name = item.xpath("./td[contains(@class,'specs')]/a/text()").get()
            mark = item.xpath(
                "./td[contains(@class,'value')]/div[contains(@class,'bl_ch_sur')]/span/span[contains(@class,'bl_med_val')]/text()").get()
            yield {"name": name, "mark": mark}

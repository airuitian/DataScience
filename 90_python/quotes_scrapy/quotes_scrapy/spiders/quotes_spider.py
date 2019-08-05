import scrapy

from quotes_scrapy.items import QuotesScrapyItem


#需要继承scrapy.Spider类
class FistSpider(scrapy.Spider): 

    # 定义蜘蛛名，运行爬虫的时候通过该名字指定运行的爬虫
    name = "quotes_spider" 
    
    # 由此方法通过下面链接爬取页面
    def start_requests(self): 
        
        # 定义爬取的链接
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'http://quotes.toscrape.com/page/3/',
            'http://quotes.toscrape.com/page/4/'
        ]
        for url in urls:
            # 爬取到的页面如何处理？提交给parse方法处理
            yield scrapy.Request(url=url, callback=self.parse) 
    
    """
        用于处理start_requests已经爬取到页面
        
    """
    def parse(self, response):
        # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        page = response.url.split("/")[-2]
        # 将网页的html保存下来
        filename = 'spider-%s.html' % page    
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)
        """
        for quote in response.css('.quote'):
            # 获得quote下面所有的标签
            # 创建Item对象
            item = QuotesScrapyItem()
            item['content'] = quote.css('span.text::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item
        """

        # 获取下一页的url
        next_page = response.css(".next a::attr(href)").extract_first()
         # 如果存在，则提交到
        if next_page is not None:
            # 转化为绝对路径
            next_page = response.urljoin(next_page)

            """
            接下来就是爬取下一页或是内容页：
            scrapy给我们提供了这么一个方法：scrapy.Request()
            我们使用其中两个参数
            一个是：我们继续爬取的链接（next_page），这里是下一页链接
            另一个是：我们要把链接提交给哪一个函数(callback=self.parse)爬取，这里是parse函数，也就是本函数
            当然，我们也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
            经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页
            yield的说明请看generator_usage.py
            """
            yield scrapy.Request(next_page, callback=self.parse)

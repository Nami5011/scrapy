import scrapy
from ten_min_scrapy.items import Post

class ScrapyBlogSpiderSpider(scrapy.Spider):
    name = 'scrapy_blog_spider'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        """
        レスポンスに対するパース処理
        """
        for post in response.css('.post-listing .post-item'):
            yield Post(
                url=post.css('div.post-header a::attr(href)').extract_first().strip(),
                title=post.css('div,post-header a::text').extract_first().strip(),
                date=post.css('div,post-header span.date a::text').extract_first().strip()
            )
        older_post_link=response.css('.blog-pagination a.text-posts-link::attr(href)').extract_first()
        if older_post_link is None:
            return
        older_post_link=response.urlJoin(older_post_link)
        yield scrapy.Request(older_post_link, callback=self.parse)

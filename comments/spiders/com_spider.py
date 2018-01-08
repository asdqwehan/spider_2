from comments.items import CommentsItem

import scrapy

class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/subject/27126455/comments?status=P'
    ]

    def parse(self, response):
        '''
        filename = 'lingshi'
        with open(filename, 'wb') as f:
            f.write(response.body)
        '''
        #sel.xpath('//div[@class="comment"]/p/text()').extract()
        #sel.xpath('//span[@class="comment-info"]/a/text()').extract()
        #sel.xpath('//div[@class="comment"]/h3/span[@class="comment-info"]/a/text()').extract()
        sel = scrapy.selector.Selector(response)

        items = []
        item = CommentsItem()
        sites = sel.xpath('//div[@class="comment"]')
        for site in sites:

            item['author'] = site.xpath('h3/span[@class="comment-info"]/a/text()').extract()
            item['comment'] = site.xpath('p/text()').extract()
            items.append(item)
            yield item
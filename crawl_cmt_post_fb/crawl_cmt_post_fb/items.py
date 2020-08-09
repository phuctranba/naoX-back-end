# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlCmtPostFbItem(scrapy.Item):
    post_id = scrapy.Field()
    content_text = scrapy.Field()
    public_time = scrapy.Field()
    user_cmt = scrapy.Field()
    image_link_cmt = scrapy.Field()
    image_content_cmt = scrapy.Field()
    number_like_cmt = scrapy.Field()
    number_love_cmt = scrapy.Field()
    number_support_cmt = scrapy.Field()
    number_haha_cmt = scrapy.Field()
    number_wow_cmt = scrapy.Field()
    number_sorry_cmt = scrapy.Field()
    number_anger_cmt = scrapy.Field()
    number_reaction_cmt = scrapy.Field()
    source_crawl_post = scrapy.Field()
    type_source_post = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlPostsFbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id_group = scrapy.Field()
    id_post = scrapy.Field()
    id_graphql = scrapy.Field()
    link_post = scrapy.Field()
    public_time_post = scrapy.Field()
    first_collect_time_post = scrapy.Field()
    lastest_collect_time_post = scrapy.Field()
    content_text_post = scrapy.Field()
    number_like_post = scrapy.Field()
    number_love_post = scrapy.Field()
    number_support_post = scrapy.Field()
    number_haha_post = scrapy.Field()
    number_wow_post = scrapy.Field()
    number_sorry_post = scrapy.Field()
    number_anger_post = scrapy.Field()
    number_share_post = scrapy.Field()
    number_cmt_post = scrapy.Field()
    number_old_cmt_post = scrapy.Field()
    number_reaction_post = scrapy.Field()
    place_post = scrapy.Field()
    hastag_post = scrapy.Field()
    image_link_post = scrapy.Field()
    image_content_post = scrapy.Field()
    source_crawl_post = scrapy.Field()
    type_source_post = scrapy.Field()
    user_post = scrapy.Field()

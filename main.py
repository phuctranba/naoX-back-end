from crawl_groups_fb.crawl_groups_fb.spiders.groups_spiders import GrousSpider
from crawl_posts_fb.crawl_posts_fb.spiders.crawl_content import ContentSpider
from crawl_cmt_post_fb.crawl_cmt_post_fb.spiders.crawl_cmt import CommentSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'data_cmt.csv'
})

# process.crawl(GrousSpider)
# process.crawl(ContentSpider)
process.crawl(CommentSpider)
process.start()

import datetime
import json
import os
import webbrowser
import re
import openpyxl
import scrapy
import csv


class ContentSpider(scrapy.Spider):
    name = "ct"

    def start_requests(self):
        urls = []
        # wb_input = openpyxl.load_workbook(filename="input.xlsx")
        #
        # sheet = wb_input.get_sheet_by_name('Sheet1')
        #
        # for row in range(10):
        #     print(sheet['A' + str(row + 1)].value)
        #     urls.append(sheet['A' + str(row + 1)].value)

        with open('/Users/ZipEnter/Work/Python/CrawlModule/crawl_posts_fb/source.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    urls.append("https://www.facebook.com/groups/" + row[0] + "/permalink/" + row[1])
                line_count += 1

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        filename = 'groupsaa.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        data_post = response.xpath("//script[contains(., 'RelayPrefetchedStreamCache')]/text()").re(
            r'data:\s*(.*extensions)')[0][:-11]
        data_post = re.sub("(\w+):", r'"\1":', data_post)
        data_json = json.loads(data_post.replace('"https"', 'https'))["feedback"]
        print(data_json)
        # Lấy đống cmt html mà không xử lý luôn dc
        data_html_cmt = response.xpath('//comment()').extract()

        html_content_post = ""
        html_template = '<html><body>%s</body></html>'

        # Lấy đống cmt nào có thẻ div chứa thông tin post
        for render_cmt_html in data_html_cmt:
            render_cmt_html = html_template % render_cmt_html.replace('<!--', '').replace('-->', '')
            sel = scrapy.Selector(text=render_cmt_html)
            html_content_post = sel.xpath('//div[@data-testid="newsFeedStream"]')
            if html_content_post:
                break

        # ghép nội dung bài viết
        contents_text = ', '.join([content_text.get() for content_text in
                                   html_content_post.xpath('//div[@data-testid="post_message"]//text()')])

        reaction_dic = {'LIKE': 0, 'LOVE': 0, 'SUPPORT': 0, 'HAHA': 0, 'WOW': 0, 'ANGER': 0, 'SORRY': 0}

        if data_json["reaction_count"]["count"] > 0:
            for react in data_json["top_reactions"]["edges"]:
                reaction_dic[react["node"]["reaction_type"]] = react["reaction_count"]

        hashtags_post = ' '.join(
            [a.get() for a in
             html_content_post.xpath('//span[@aria-label="hashtag"]/following-sibling::span[1]/text()')])

        imgs_link_post = ' '.join(
            [link_img.attrib["data-ploi"] for link_img in html_content_post.xpath('//a[@rel="theater"]')])

        imgs_content_post = ', '.join(
            [link_img.attrib["alt"] for link_img in html_content_post.xpath('//a[@rel="theater"]/following::img')])

        imgs_content_post = imgs_content_post.replace("Trong hình ảnh có thể có:", '')
        imgs_content_post = imgs_content_post.replace("Image may contain:", '')
        imgs_content_post = imgs_content_post.replace("Không có mô tả ảnh", '')
        imgs_content_post = imgs_content_post.replace("No photo description available", '')
        imgs_content_post = imgs_content_post.replace("văn bản cho biết", '')
        imgs_content_post = imgs_content_post.replace("text that says", '')
        imgs_content_post = imgs_content_post.replace("  ", ' ')

        place_post = ""
        if html_content_post.xpath('//a[@class="profileLink"]/text()'):
            place_post = html_content_post.xpath(
                '//a[@class="profileLink"]/text()').get()
            if html_content_post.xpath('//span[@role="presentation"]/following-sibling::a[1]/text()'):
                place_post = place_post + ', ' + html_content_post.xpath(
                    '//span[@role="presentation"]/following-sibling::a[1]/text()').get()

        yield {
            'group_id': data_json["associated_group"]["id"],
            'post_id': data_json["subscription_target_id"],
            'id_graphql': data_json["id"],
            'link_post': "https://www.facebook.com/groups/" + data_json["associated_group"][
                "id"] + "/permalink/" + data_json["subscription_target_id"],
            'public_time_post': datetime.date.fromtimestamp(
                int(html_content_post.xpath("//abbr").attrib['data-utime'])),
            'first_collect_time_post': datetime.date.today(),
            'lastest_collect_time_post': datetime.date.today(),
            'content_text_post': contents_text.replace('\n', ' '),
            'number_like_post': reaction_dic['LIKE'],
            'number_love_post': reaction_dic['LOVE'],
            'number_support_post': reaction_dic['SUPPORT'],
            'number_haha_post': reaction_dic['HAHA'],
            'number_wow_post': reaction_dic['WOW'],
            'number_sorry_post': reaction_dic['SORRY'],
            'number_anger_post': reaction_dic['ANGER'],
            'number_share_post': data_json["share_count"]["count"],
            'number_cmt_post': data_json["comment_count"]["total_count"],
            'number_old_cmt_post': data_json["comment_count"]["total_count"],
            'number_reaction_post': data_json["reaction_count"]["count"],
            'place_post': place_post,
            'hastag_post': hashtags_post,
            'image_link_post': imgs_link_post,
            'image_content_post': imgs_content_post.replace('\n', ' '),
            'source_crawl_post': "FACEBOOK",
            'type_source_post': "SOCIAL_NETWORK",
            'user_post': data_json["owning_profile"]["id"],
        }

import datetime
import json
import os
import webbrowser

import openpyxl
import scrapy


class GrousSpider(scrapy.Spider):
    name = "gf"

    time = 1
    COUNT_MAX = 100
    count = 0
    def start_requests(self):

        urls = [
            "https://mbasic.facebook.com/groups/odayaka.vn"
        ]

        # wb_input = openpyxl.load_workbook(filename="input.xlsx")
        #
        # sheet = wb_input.get_sheet_by_name('Sheet1')
        #
        # for row in range(10):
        #     print(sheet['A' + str(row + 1)].value)
        #     urls.append(sheet['A' + str(row + 1)].value)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):


        flag_continue = True
        # list_post = []

        filename = 'groups.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        container_groups_post = response.xpath('//div[@id="m_group_stories_container"]/div[1]/div')
        # webbrowser.open_new_tab('file://' + os.path.realpath("groups.html"))

        next_page = response.xpath('//*[@id="m_group_stories_container"]/div[2]/a').extract_first()
        next_page_url = response.xpath('//*[@id="m_group_stories_container"]/div[2]/a').attrib['href']

        group_id = next_page_url.split("?")[0].split("/")[2]

        # group_id = json.loads(response.xpath('//div[@class="bd bf bp"]').attrib['data-ft'])["page_id"]
        # print("=====================", response.xpath('//div[@class="bd bf bp"]'))
        for post in container_groups_post:
            post_param = json.loads(post.attrib['data-ft'])
            publish_time = datetime.date.fromtimestamp(
                post_param["page_insights"][group_id]["post_context"]["publish_time"])
            date_compare = datetime.date(2010, 1, 1)

            if "mf_story_key" in post_param:
                if publish_time > date_compare:
                    post_id = post_param["mf_story_key"]
                    # list_post.append(post_id)
                    yield {
                        'group_id': group_id,
                        'post_id': post_id
                    }
                else:
                    flag_continue = False
                    break

        # for id_post in list_post:
        #     yield scrapy.Request(url=("https://www.facebook.com/groups/" + group_id + "/permalink/" + id_post),
        #                          callback=self.parse_post)

        self.count = self.count + 1
        if next_page is not None and flag_continue and self.count < self.COUNT_MAX:
            yield scrapy.Request(
                response.urljoin("https://mbasic.facebook.com" + next_page_url))

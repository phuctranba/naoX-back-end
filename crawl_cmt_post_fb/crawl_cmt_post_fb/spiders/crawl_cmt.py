import datetime
import json
import os
import webbrowser
import re
import openpyxl
import scrapy
import csv


class CommentSpider(scrapy.Spider):
    name = "cmt"

    variablesform = r'{"after":%s,"before":null,"displayCommentsFeedbackContext":"{\"bump_reason\":0,' \
                    r'\"comment_expand_mode\":1,\"comment_permalink_args\":{\"comment_id\":null,' \
                    r'\"reply_comment_id\":null,\"filter_non_supporters\":null},\"interesting_comment_fbids\":[],' \
                    r'\"is_location_from_search\":false,\"last_seen_time\":1595923028,' \
                    r'\"log_ranked_comment_impressions\":false,\"probability_to_comment\":0,\"story_location\":6,' \
                    r'\"story_type\":0}","displayCommentsContextEnableComment":false,' \
                    r'"displayCommentsContextIsAdPreview":false,"displayCommentsContextIsAggregatedShare":false,' \
                    r'"displayCommentsContextIsStorySet":false,"feedLocation":"GROUP_PERMALINK",' \
                    r'"feedbackID":"%s","feedbackSource":2,"first":50,' \
                    r'"focusCommentID":null,"includeNestedComments":false,"isInitialFetch":false,"isComet":false,' \
                    r'"containerIsFeedStory":true,"containerIsWorkplace":false,"containerIsLiveStory":false,' \
                    r'"containerIsTahoe":false,"last":null,"scale":1,"topLevelViewOption":null,' \
                    r'"useDefaultActor":true,"viewOption":null,"UFI2CommentsProvider_commentsKey":null} '

    def start_requests(self):
        variables = []
        # wb_input = openpyxl.load_workbook(filename="input.xlsx")
        #
        # sheet = wb_input.get_sheet_by_name('Sheet1')

        # for row in range(10):
        #     print(sheet['A' + str(row + 1)].value)
        #     urls.append(sheet['A' + str(row + 1)].value)

        with open('data_to_cmt.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    variables.append(self.variablesform % ('null', row[2]))
                line_count += 1

        for variable in variables:
            frmdata = {
                "variables": variable,
                "doc_id": '3235202059927512'}
            yield scrapy.FormRequest(url="https://www.facebook.com/api/graphql/", method='POST',
                                     formdata=frmdata,
                                     callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.body)["data"]["feedback"]
        print(json_data)

        list_cmt = json_data["display_comments"]["edges"]

        if json_data["display_comments"]["page_info"]["has_next_page"]:
            variables = self.variablesform % (
                '"' + json_data["display_comments"]["page_info"]["end_cursor"] + '"', json_data["id"])
            frmdata = {
                "variables": variables,
                "doc_id": '3235202059927512'}
            yield scrapy.FormRequest(url="https://www.facebook.com/api/graphql/", method='POST',
                                     formdata=frmdata,
                                     callback=self.parse)

        for detail_cmt in list_cmt:
            reaction_dic = {'LIKE': 0, 'LOVE': 0, 'SUPPORT': 0, 'HAHA': 0, 'WOW': 0, 'ANGER': 0, 'SORRY': 0}
            if detail_cmt["node"]["feedback"]["reactors"]["count"] > 0:
                for react in detail_cmt["node"]["feedback"]["top_reactions"]["edges"]:
                    reaction_dic[react["node"]["reaction_type"]] = react["reaction_count"]

            imgs_link_cmt = ' '.join(
                [link_img["media"]["image_396"]["uri"] if link_img["media"]["__typename"] == "Photo" is not None else ""
                 for
                 link_img in detail_cmt["node"]["attachments"]])

            image_content_cmt = ' '.join(
                [link_img["media"]["accessibility_caption"] if "accessibility_caption" in link_img["media"] else ""
                 for link_img in detail_cmt["node"]["attachments"]])

            image_content_cmt = image_content_cmt.replace("Trong hình ảnh có thể có:", '')
            image_content_cmt = image_content_cmt.replace("Image may contain:", '')
            image_content_cmt = image_content_cmt.replace("Không có mô tả ảnh", '')
            image_content_cmt = image_content_cmt.replace("No photo description available", '')
            image_content_cmt = image_content_cmt.replace("văn bản cho biết", '')
            image_content_cmt = image_content_cmt.replace("text that says", '')
            image_content_cmt = image_content_cmt.replace("  ", ' ')

            yield {
                'post_id': json_data["subscription_target_id"],
                'content_text': detail_cmt["node"]["preferred_body"]["text"].replace('\n', ' ') if detail_cmt["node"][
                                                                                                       "preferred_body"] is not None else "",
                'public_time': datetime.date.fromtimestamp(int(detail_cmt["node"]["created_time"])),
                'user_cmt': detail_cmt["node"]["author"]["id"],
                'image_link_cmt': imgs_link_cmt,
                'image_content_cmt': image_content_cmt.replace('\n', ' '),
                'number_like_cmt': reaction_dic['LIKE'],
                'number_love_cmt': reaction_dic['LOVE'],
                'number_support_cmt': reaction_dic['SUPPORT'],
                'number_haha_cmt': reaction_dic['HAHA'],
                'number_wow_cmt': reaction_dic['WOW'],
                'number_sorry_cmt': reaction_dic['SORRY'],
                'number_anger_cmt': reaction_dic['ANGER'],
                'number_reaction_cmt': detail_cmt["node"]["feedback"]["reactors"]["count"],
                'source_crawl_post': "FACEBOOK",
                'type_source_post': "SOCIAL_NETWORK",
            }

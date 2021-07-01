#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.6/site-packages')

import tweepy
from time import sleep
import schedule
import time
import settings

def tweet():
    """
    docstring
    """

    print('ツイート中...')
        
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth ,wait_on_rate_limit = True)

    # つぶやきたい内容の文字列を生成
    message = str("Today Pixiv Daily Top 3.\n")

    # 複数画像を添付
    file_names=["illusts/illust_id_1.jpg", "illusts/illust_id_2.jpg", "illusts/illust_id_3.jpg"]
    media_ids = []
    for filename in file_names:
        res = api.media_upload(filename)
        media_ids.append(res.media_id)

    # 文字列と複数画像の投稿
    api.update_status(status=message, media_ids=media_ids)

    print('ツイート完了!')


if __name__ == '__main__':
    tweet()
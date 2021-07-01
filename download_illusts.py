#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import datetime

if sys.version_info >= (3, 0):
    import imp
    imp.reload(sys)
else:
    reload(sys)
    sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

from pixivpy3 import *

_USERNAME = "pix-sns"
_PASSWORD = "pixsnsofficial"


def download():

    # 昨日のランキング
    date_today = datetime.date.today()
    date_yesterday = date_today - datetime.timedelta(days=1)

    sni = False
    if not sni:
        api = AppPixivAPI()
    else:
        api = ByPassSniApi()  # Same as AppPixivAPI, but bypass the GFW
        api.require_appapi_hosts()
    api.login(_USERNAME, _PASSWORD)

    # get rankings
    json_result = api.illust_ranking('day', date=date_yesterday)

    directory = "illusts"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # download top3 day rankings to 'illusts' dir
    for idx, illust in enumerate(json_result.illusts[:4]):
        image_url = illust.meta_single_page.get('original_image_url', illust.image_urls.large)
        print("%s: %s" % (illust.title, image_url))

        # try four args in MR#102
        if idx == 0:
            name = "illust_id_1.jpg"
            api.download(image_url, path=directory, name=name)
        elif idx == 1:
            # url_basename = os.path.basename(image_url)
            # extension = os.path.splitext(url_basename)[1]
            name = "illust_id_2.jpg"
            api.download(image_url, path=directory, name=name)
        elif idx == 2:
            name = "illust_id_3.jpg"
            api.download(image_url, path=directory, name=name)
        else:
            # path will not work due to fname is a handler
            name = "illust_id_4.jpg"
            api.download(image_url, path=directory, name=name)


if __name__ == '__main__':
    download()
    
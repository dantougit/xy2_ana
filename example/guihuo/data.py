#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-12
# @Author  : haopingan


import sys
sys.path.insert(0, "/home/haopingan/luan/xy2_ana/")

from models import crawl



if __name__ == "__main__":
    guihuo = crawl.Crawl()

    res = guihuo.common_crawl(page=1, server_type="sishang", kind="wuqi", price_min=10000, price_max=188888, suit_require="gengu", total_attr={"jiaqiangguihuo": 48, "guihuokuangbaojilv": 4, "guihuokuangbaochengdu": 10}, debug=True)

    # res = guihuo.common_crawl(page=1, server_type="sishang", kind="xianglian", suit_require="", price_min=8000, price_max=188888, total_attr={"guihuokuangbaojilv": 17}, debug=True)
    

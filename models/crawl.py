#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28
# @Author  : haozhuolin

import sys
import time
import json
import random
import datetime

import requests


class Crawl(object):
    def __init__(self):
        self.host = ""
        self.host = "https://xy2.cbg.163.com/cgi-bin/search.py"

        self.kind = {
            "nanmao": 10,
            "nvmao": 11,
            "xianglian": 12,
            "xie": 13,
            "nanyi": 14,
            "nvyi": 15,
            "wuqi": 16,
        }

        self.suit_require = {
            "minjie": 1,
            "gengu": 2,
            "lingxing": 3,
            "liliang": 4,
            "wu": 5,
            "": "",
        }

        self.server_type = {
            "": "",
            "sishang": 3,
            "sixia": 2,
        }


    def get_json(self, url, params):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.1"}
        response = requests.get(url, headers=headers, timeout=5, params=params)
        print(response.text)
        data = response.json()
        return data

    def common_crawl(self,
                    act="overall_search_equip",
                    page=1,
                    price_min=0,
                    price_max=100000000,
                    server_type="",
                    kind="wuqi",
                    suit_require="liliang",
                    basic_attr={},
                    lian_hua_attr={},
                    total_attr={},
                    debug=False
        ):

        params = {
            # 装备搜索
            "act": act,

            # 页数
            "page": page,

            # 最低价格
            "price_min": price_min,

            # 最高价格
            "price_max": price_max,

            # 服务器类型
            "server_type": self.server_type[server_type],

            # 装备类型
            "kindid": self.kind[kind],

            # 装备需求
            "suit_require": self.suit_require[suit_require],

            # 基础属性    
            "basic_attr": basic_attr,

            # 炼化属性
            "lian_hua_attr": lian_hua_attr,

            # 全部属性
            "total_attr": total_attr,
            
            # 随机数
            "random": datetime.datetime.now().strftime("%a %b %d %Y %H:%M:%S GMT+0800 (中国区标准时间)")
        }

        # 过滤空属性
        params = {k: v for k, v in params.items() if v}

        # 如果是json需要dump
        params = {k: json.dumps(v) if isinstance(v, dict) else v for k, v in params.items()}
        
        res = []
        while True:
            print(params["page"])
            tmp = self.get_json(self.host, params)
            if 'msg' in tmp:
                res.extend(tmp['msg'])
                if debug:
                    for t in tmp['msg']:
                        print(json.dumps([t["attrs"], "https://xy2.cbg.163.com/equip?s=%s&eid=%s" % (t["serverid"], t["eid"]), t['price']/100], ensure_ascii=False))

            time.sleep(5 + random.random())

            # 如果是最后一页，跳出
            if "is_last_page" not in tmp["paging"] or tmp["paging"]["is_last_page"]:
                break

            params["page"] += 1

        res = [[data["attrs"], "https://xy2.cbg.163.com/equip?s=%s&eid=%s" % (data["serverid"], data["eid"]), data['price']/100] for data in res]
        return res
        


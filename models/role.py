#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-28
# @Author  : haozhuolin

import sys
import time
import json
import datetime

from crawl import Crawl

class RoleCrawl(Crawl):
    def __init__(self):
        super(Crawl, self).__init__()
        self.load_server()
        self.load_sex()

    def load_server(self):
        server = json.load(open('../config/server_list.json'))
        self.servers = []
        for k, v in server.items():
            for vv in v[1]:
                self.servers.append(vv[0])

    def load_sex(self):
        self.sex = ['1001', '1002', '1003', '1004', '1005', '2001', '2002', '2003', '2004', '2005']

    def common_crawl(self):
        ## 获取全部在投
        host = "https://xy2.cbg.163.com/cgi-bin/search.py?act=overall_search_role&price_min=0&price_max=100000000"

        ## 遍历server ids
        for server in self.servers:
            host1 = host + ("&serverid=%s" % server)
            ## 遍历性别种族
            for sex in self.sex:
                host2 = host1 + ("&sex_race=%s" % sex)
                ## 遍历页数
                num = 1
                try:
                    num = self.get_json(host2)['paging']['total_pages']
                except Exception as e:
                    print("get_num_error, %s" % host2)

                for i in range(1, num + 1):
                    host3 = host2 + ("&page=%s" % i)
                    roles = []
                    try:
                        roles = self.get_json(host3)['msg']
                    except Exception as e:
                        print("get_json_msg, %s" % host3)

                    self.output(roles)
                    time.sleep(10)

    def output(self, roles):
        today=datetime.date.today()
        fw = open('roles.%s' % today, 'a+')
        for role in roles:
            role_eid = role['eid']
            s = role['serverid']
            fw.write("https://xy2.cbg.163.com/equip?s=%s&eid=%s&view_loc=overall_search\n" % (s, role_eid))
        fw.close()

    
if __name__ == '__main__':
    role_crawl = RoleCrawl()
    bg = time.time() - 3600 * 24

    while True:
        if time.time() - bg < 3600 * 24:
            time.sleep(600)
            continue
        
        bg = time.time()
        try:
            role_crawl.common_crawl()
        except Exception as e:
            print("error, %s" % e)
            exit(0)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-12
# @Author  : haopingan


import sys
import json
import itertools

class Equip():
    def __init__(self, hushi=0, qiang=0, ke=0, kuangbao=0, chengdu=0, price=0, url=""):
        self.hushi = hushi
        self.qiang = qiang
        self.ke = ke
        self.kuangbao = kuangbao
        self.chengdu = chengdu
        self.price = price
        self.url = url

    def get_shanghai(self):
        pingmiao = (1 + self.qiang / 100) * (1 + self.hushi / 100) * (1 + self.ke / 200)
        kuangbao = (1 + self.qiang / 100) * (1 + self.hushi / 100) * (1 + self.ke / 200) * (1.5 + self.chengdu / 100)
        self.shanghai = self.kuangbao / 100 * kuangbao + (1 - self.kuangbao / 100) * pingmiao
        return self.shanghai

    def display(self):
        print("hushi: %s\tqiang: %s\tke: %s\tkuangbao: %s\tchengdu: %s\tprice: %s\tshanghai: %s\turl: %s" % (self.hushi, self.qiang, self.ke, self.kuangbao, self.chengdu, self.price, self.get_shanghai(), self.url))

    def __add__(self, other):
        tmp = Equip()
        tmp.hushi = self.hushi + other.hushi
        tmp.qiang = self.qiang + other.qiang
        tmp.ke = self.ke + other.ke
        tmp.kuangbao = self.kuangbao + other.kuangbao
        tmp.chengdu = self.chengdu + other.chengdu
        tmp.price = self.price + other.price
        tmp.url = self.url + " " + other.url
        return tmp


basic = Equip(10, 68.5, 177.5, 33, 0)

wuqis = []
with open("./wuqi") as fi:
    for line in fi:
        try:
            arr = json.loads(line.strip())
        except Exception as e:
            continue

        if not isinstance(arr, list):
            continue
        
        attr, url, price = arr

        price = float(price)
        if "s=19&" not in url:
            price += 150

        wuqi = Equip()
        wuqi.url = url
        wuqi.price = price

        for name in ["基本属性", "炼化属性", "炼器属性", "追加属性"]:
            wuqi.hushi += attr.get(name, {}).get("忽视抗鬼火", 0)
            wuqi.qiang += attr.get(name, {}).get("加强鬼火", 0)
            wuqi.ke += attr.get(name, {}).get("强力克水", 0)
            wuqi.kuangbao += attr.get(name, {}).get("鬼火狂暴几率", 0)
            wuqi.chengdu += attr.get(name, {}).get("鬼火狂暴程度", 0)
        
        # wuqi.display()
        wuqis.append(wuqi)

xianglians = []
with open("./xianglian") as fi:
    for line in fi:
        try:
            arr = json.loads(line.strip())
        except Exception as e:
            continue

        if not isinstance(arr, list):
            continue
        
        attr, url, price = arr

        price = float(price)
        if "s=19&" not in url:
            price += 150

        xianglian = Equip()
        xianglian.url = url
        xianglian.price = price

        for name in ["基本属性", "炼化属性", "炼器属性", "追加属性"]:
            xianglian.hushi += attr.get(name, {}).get("忽视抗鬼火", 0)
            xianglian.qiang += attr.get(name, {}).get("加强鬼火", 0)
            xianglian.ke += attr.get(name, {}).get("强力克水", 0)
            xianglian.kuangbao += attr.get(name, {}).get("鬼火狂暴几率", 0)
            xianglian.chengdu += attr.get(name, {}).get("鬼火狂暴程度", 0)
        
        # xianglian.display()
        xianglians.append(xianglian)


xingkas = [
            Equip(hushi=9, qiang=15.4, ke=0, kuangbao=0, chengdu=0, price=400),
            Equip(hushi=9, qiang=0, ke=0, kuangbao=10.4, chengdu=0, price=350),
            Equip(hushi=0, qiang=15.4, ke=0, kuangbao=10.4, chengdu=0, price=400),
            Equip(hushi=9, qiang=0, ke=0, kuangbao=0, chengdu=19.3, price=550),
            Equip(hushi=0, qiang=15.4, ke=0, kuangbao=0, chengdu=19.3, price=430),
            Equip(hushi=0, qiang=0, ke=0, kuangbao=0, chengdu=37.5, price=750),
            Equip(hushi=0, qiang=0, ke=0, kuangbao=10.4, chengdu=19.3, price=400)
        ]

hushenfus = [
            Equip(hushi=4.6, qiang=5.7, ke=29, kuangbao=5.7, chengdu=5.7, price=400),
            Equip(hushi=4.6, qiang=5.7, ke=29, kuangbao=0, chengdu=0, price=400),
            Equip(hushi=4.6, qiang=5.7, ke=12, kuangbao=5.7, chengdu=0, price=400),
            Equip(hushi=4.6, qiang=5.7, ke=12, kuangbao=0, chengdu=5.7, price=400),
            Equip(hushi=4.6, qiang=0, ke=29, kuangbao=5.7, chengdu=0, price=400),
            Equip(hushi=4.6, qiang=0, ke=29, kuangbao=0, chengdu=5.7, price=400),
            Equip(hushi=4.6, qiang=0, ke=12, kuangbao=5.7, chengdu=5.7, price=400),
            Equip(hushi=0, qiang=5.7, ke=29, kuangbao=5.7, chengdu=0, price=400),
            Equip(hushi=0, qiang=5.7, ke=29, kuangbao=0, chengdu=5.7, price=400),
            Equip(hushi=0, qiang=5.7, ke=12, kuangbao=5.7, chengdu=5.7, price=400),
            Equip(hushi=0, qiang=0, ke=29, kuangbao=5.7, chengdu=5.7, price=400),
        ]


for arr in itertools.product(wuqis, xianglians, xingkas, hushenfus):
    wuqi, xianglian, xingka, hushenfu = arr

    res = basic + wuqi + xianglian + xingka + hushenfu
    
    if res.kuangbao >= 80 and res.get_shanghai() >= 10:
        res.display()

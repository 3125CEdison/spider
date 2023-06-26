import json
import random
import re
import time
from collections import Counter
import pandas as pd
import pymysql
import requests
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from model.config import BASE_url, _score_url, scoreType_url, page_url, other_url, url, headers, url_inputs

url_input = 'https://item.jd.com/10034116992996.html'  # input("请输入京东商品网址：")
id = ''.join(re.findall(r'com/(.*?)\.html', url_input))
maxpage = 1
ids = []
mps = []  # 好评中评差评最大页数
baseurls = Queue()  # 待爬取url队列[]
jsons = Queue()  # 待解析json文档队列
outputs = Queue()  # 提取信息后的json文档
for i in url_inputs:
    id1 = ''.join(re.findall(r'com/(.*?)\.html', i))
    ids.append(id1)


def get_sum():
    if url_input in url_inputs:
        for d in ids:
            query = {
                "callback": "fetchJSON_comment98",  # 默认
                "productId": d,  # 商品ID
                "score": 3,  # 差评1 中评2 好评3
                "sortType": "6",  # 默认
                "page": "0",  # 当前页码
                "pageSize": "10",  # 展示的评论数
                "isShadowSku": "0",  # 默认
                "fold": "1",  # 默认
            }
            # time.sleep(random.randint(2, 4))
            res = requests.get(url=url, headers=headers, params=query)
            res = json.loads(re.match(r"^fetchJSON_comment98\((.+)\);", res.text).group(1))
            pc = res["productCommentSummary"]
            goodC = pc["goodCountStr"].replace("+", '')
            genC = pc["generalCountStr"].replace("+", '')
            poorC = pc["poorCountStr"].replace("+", '')
            videoC = pc["videoCountStr"].replace("+", '')
            afterC = pc["afterCountStr"].replace("+", '')
            showC = pc["showCountStr"].replace("+", '')
            product = res["comments"][0]["referenceName"].replace(" ", '').replace("\n", ' ')
            product_id = pc["productId"]
            db = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
            cursor = db.cursor()
            sql2 = """INSERT IGNORE INTO jdspider.sum VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                        """ % (product, product_id, goodC, genC, poorC, videoC, afterC, showC)

            try:
                cursor.execute(sql2)
                db.commit()
                # print("插入成功")
            finally:
                # print("插入失败")
                db.rollback()

            sql_updata1 = {
                "update jdspider.sum set product = '亚瑟士ASICS' where product = "
                "'亚瑟士ASICS男鞋透气跑步鞋耐磨越野跑鞋耐磨运动鞋GEL-KAHANA8深灰色42.5'",
                "update jdspider.sum set product = '彪马PUMA' where product = "
                "'彪马（PUMA）官方男女同款低帮情侣鞋撞色复古缓震跑步训练休闲鞋R78373117黑色-白-0138'",
                "update jdspider.sum set product = '耐克NIKE' where product = "
                "'耐克NIKE跑步鞋男缓震透气REVOLUTION6运动鞋DC3728-003黑41'",
                "update jdspider.sum set product = 'NEWBALANCE' where product = "
                "'NEWBALANCENB官方男鞋女鞋2002R系列时尚舒适复古运动休闲鞋中灰色ML2002RA42(脚长26.5cm)'",
                "update jdspider.sum set product = '斯凯奇Skechers' where product = "
                "'斯凯奇黑白金丨夏季透气情侣老爹鞋复古增高休闲运动鞋男女款经典熊猫鞋'",
                "update jdspider.sum set product = '安踏ANTA' where product = "
                "'安踏毒刺丨跑步鞋男2023夏季轻便减震男士休闲鞋运动鞋子男【毒刺2】象牙白/幻景蓝-48.5(男42)'",
                "update jdspider.sum set product = '阿迪达斯ADIDAS' where product = "
                "'阿迪达斯ADIDAS男子跑步系列DURAMO10运动跑步鞋GW833642码UK8码'",
                "update jdspider.sum set product = '匹克PEAK' where product = "
                "'匹克态极3.0跑步鞋男子夏季透气网面轻便男鞋减震休闲运动鞋男E11617H'"}
            for sqlupdata2 in sql_updata1:
                try:
                    cursor.execute(sqlupdata2)
                    db.commit()
                finally:
                    db.rollback()

            db.close()


def get_maxpage():  # 获取好评中评差评的最大页数
    for _score in range(3, 0, -1):
        query = {
            "callback": "fetchJSON_comment98",  # 默认
            "productId": id,  # 商品ID
            "score": _score,  # 差评1 中评2 好评3
            "sortType": "6",  # 默认
            "page": "0",  # 当前页码
            "pageSize": "10",  # 展示的评论数
            "isShadowSku": "0",  # 默认
            "fold": "1",  # 默认
        }
        # time.sleep(random.randint(2, 4))
        res = requests.get(url=url, headers=headers, params=query)
        res = json.loads(re.match(r"^fetchJSON_comment98\((.+)\);", res.text).group(1))
        mp = res["maxPage"]
        mps.append(mp)
        print(mp)
    print('好评中评差评页数分别为{}'.format(mps))


def start_urls():  # 生成待爬取url队列
    if url_input in url_inputs:
        for d in ids:
            for page in range(5):
                baseurl1 = "{}{}{}{}{}{}{}{}".format(BASE_url, d, _score_url, 3, scoreType_url, page_url, page,
                                                     other_url)
                baseurls.put(baseurl1)
                print(baseurl1)
            for page in range(5):
                baseurl2 = "{}{}{}{}{}{}{}{}".format(BASE_url, d, _score_url, 2, scoreType_url, page_url, page,
                                                     other_url)
                baseurls.put(baseurl2)
                print(baseurl2)
            for page in range(5):
                baseurl3 = "{}{}{}{}{}{}{}{}".format(BASE_url, d, _score_url, 1, scoreType_url, page_url, page,
                                                     other_url)
                baseurls.put(baseurl3)
                print(baseurl3)
        # print('一共构造了{}条URL'.format(len(baseurls)))

    else:
        for page in range(mps[0]):
            baseurl1 = "{}{}{}{}{}{}{}{}".format(BASE_url, id, _score_url, 3, scoreType_url, page_url, page,
                                                 other_url)
            baseurls.put(baseurl1)
        for page in range(mps[1]):
            baseurl2 = "{}{}{}{}{}{}{}{}".format(BASE_url, id, _score_url, 2, scoreType_url, page_url, page,
                                                 other_url)
            baseurls.put(baseurl2)
        for page in range(mps[2]):
            baseurl3 = "{}{}{}{}{}{}{}{}".format(BASE_url, id, _score_url, 1, scoreType_url, page_url, page,
                                                 other_url)
            baseurls.put(baseurl3)
        # print('一共构造了{}条URL'.format(len(baseurls)))
        # print(baseurls)


def crawler(e: Event):
    while not e.set():
        baseurl = baseurls.get()
        time.sleep(random.randint(2, 4))
        res = requests.get(baseurl, headers=headers)
        with res:
            if res.status_code == 200:
                doc = res.text
                # print('状态码：{}'.format(res.status_code), doc)
            else:
                print(res.status_code)
            jsons.put(doc)


def parse(e: Event):
    while not e.set():
        doc = jsons.get()
        comment_dict = json.loads(re.match(r"^fetchJSON_comment98\((.+)\);", doc).group(1))
        # print(comment_dict)
        comment_data = comment_dict["comments"]
        product_id = comment_dict["productCommentSummary"]["productId"]
        for item in comment_data:
            plusAvailable = item["plusAvailable"]
            user_id = item["id"]  # 用户id
            nickname = item["nickname"]  # 用户名称
            comment = item["content"].replace(" ", '').replace("\n", ' ')
            creationTime = item["creationTime"]  # 评论时间
            product = item["referenceName"].replace(" ", '')  # 商品名称
            comment_level = item["score"]  # 评论星数
            info_dict = {
                "user_id": user_id,
                "nickname": nickname,
                "content": comment,
                "creationTime": creationTime,
                "referenceName": product,
                "score": comment_level,
            }

            if comment_level >= 4:
                comment_type = item["_score"] = "好评"

            elif comment_level < 2:
                comment_type = item["_score"] = "差评"

            else:
                comment_type = item["_score"] = "中评"

            if plusAvailable == 201:
                member = info_dict["plusAvailable"] = "plus会员"
            else:
                member = info_dict["plusAvailable"] = "普通会员"

            val = {
                '评论等级': comment_type,
                '星级': comment_level,
                '用户ID': user_id,
                '会员属性': member,
                '用户名': nickname,
                '评论时间': creationTime,
                '商品名称': product,
                '商品ID': product_id,
                '评论内容': comment.format(**info_dict)
            }
            outputs.put(val)
            write_db(comment_type, comment_level, user_id, member, nickname, creationTime, product, product_id, comment)


def write_db(comment_type, comment_level, user_id, member, nickname, creationTime, product, product_id, comment):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cursor = db.cursor()

    sql1 = """INSERT IGNORE INTO jdspider.jd_comment VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
            """ % (comment_type, comment_level, user_id, member, nickname, creationTime, product, product_id, comment)

    try:
        cursor.execute(sql1)
        db.commit()
    except:
        print("插入失败")
        db.rollback()

    sql_delete = "delete from jdspider.jd_comment where comment like '%填写评价内容%' "

    try:
        cursor.execute(sql_delete)
        db.commit()
    finally:
        db.rollback()

    sql_updata = {
        "update jdspider.jd_comment set product = '亚瑟士ASICS' where product = "
        "'亚瑟士ASICS男鞋透气跑步鞋耐磨越野跑鞋耐磨运动鞋GEL-KAHANA8深灰色42.5'",
        "update jdspider.jd_comment set product = '彪马PUMA' where product = "
        "'彪马（PUMA）官方男女同款低帮情侣鞋撞色复古缓震跑步训练休闲鞋R78373117黑色-白-0138'",
        "update jdspider.jd_comment set product = '耐克NIKE' where product = "
        "'耐克NIKE跑步鞋男缓震透气REVOLUTION6运动鞋DC3728-003黑41'",
        "update jdspider.jd_comment set product = 'NEWBALANCE' where product = "
        "'NEWBALANCENB官方男鞋女鞋2002R系列时尚舒适复古运动休闲鞋中灰色ML2002RA42(脚长26.5cm)'",
        "update jdspider.jd_comment set product = '斯凯奇Skechers' where product = "
        "'斯凯奇黑白金丨夏季透气情侣老爹鞋复古增高休闲运动鞋男女款经典熊猫鞋'",
        "update jdspider.jd_comment set product = '安踏ANTA' where product = "
        "'安踏毒刺丨跑步鞋男2023夏季轻便减震男士休闲鞋运动鞋子男【毒刺】象牙白/幻景蓝-48.5(男42)'",
        "update jdspider.jd_comment set product = '阿迪达斯ADIDAS' where product = "
        "'阿迪达斯ADIDAS男子跑步系列DURAMO10运动跑步鞋GW833642码UK8码'",
        "update jdspider.jd_comment set product = '匹克PEAK' where product = "
        "'匹克态极3.0跑步鞋男子夏季透气网面轻便男鞋减震休闲运动鞋男E11617H'"}
    for sqlupdata in sql_updata:
        try:
            cursor.execute(sqlupdata)
            db.commit()
        finally:
            db.rollback()

    db.close()


# def persist(e: Event):  #
#     while not e.set():
#         if url_input in url_inputs:
#             engine = create_engine('mysql+pymysql://root:123456@localhost:3306/jdspider', echo=True)
#             sql1 = "SELECT * FROM jdspider.jd_comment WHERE product='彪马PUMA'"
#             sql2 = "SELECT * FROM jdspider.jd_comment WHERE product='NEWBALANCE'"
#             sql3 = "SELECT * FROM jdspider.jd_comment WHERE product='阿迪达斯ADIDAS'"
#             sql4 = "SELECT * FROM jdspider.jd_comment WHERE product='安踏ANTA'"
#             sql5 = "SELECT * FROM jdspider.jd_comment WHERE product='耐克NIKE'"
#             sql6 = "SELECT * FROM jdspider.jd_comment WHERE product='匹克PEAK'"
#             sql7 = "SELECT * FROM jdspider.jd_comment WHERE product='斯凯奇Skechers'"
#             sql8 = "SELECT * FROM jdspider.jd_comment WHERE product='亚瑟士ASICS'"
#             dfs1 = pd.read_sql(sql1, engine)
#             dfs2 = pd.read_sql(sql2, engine)
#             dfs3 = pd.read_sql(sql3, engine)
#             dfs4 = pd.read_sql(sql4, engine)
#             dfs5 = pd.read_sql(sql5, engine)
#             dfs6 = pd.read_sql(sql6, engine)
#             dfs7 = pd.read_sql(sql7, engine)
#             dfs8 = pd.read_sql(sql8, engine)
#             dfs1.to_csv(r'./csv/彪马PUMA.csv', index=True)
#             dfs2.to_csv(r'./csv/NEWBALANCE.csv', index=True)
#             dfs3.to_csv(r'./csv/阿迪达斯ADIDAS.csv', index=True)
#             dfs4.to_csv(r'./csv/安踏ANTA.csv', index=True)
#             dfs5.to_csv(r'./csv/耐克NIKE.csv', index=True)
#             dfs6.to_csv(r'./csv/匹克PEAK.csv', index=True)
#             dfs7.to_csv(r'./csv/斯凯奇Skechers.csv', index=True)
#             dfs8.to_csv(r'./csv/亚瑟士ASICS.csv', index=True)


# get_sum()
# get_maxpage()
# event = Event()
# excutor = ThreadPoolExecutor(10)
# excutor.submit(start_urls)
# excutor.submit(write_db)
# excutor.submit(persist, event)
if __name__ == '__main__':
    event = Event()
    excutor = ThreadPoolExecutor(10)
    # excutor.submit(persist, event)
    get_sum()
    get_maxpage()
    excutor.submit(start_urls)
    for i in range(2):
        excutor.submit(crawler, event)
    for i in range(10):
        excutor.submit(parse, event)
    excutor.submit(write_db)

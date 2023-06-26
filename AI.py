import time
from concurrent.futures import ThreadPoolExecutor
from mysql import puma, adidas, anta, asics, peak, Skechers, new, nike
import pandas as pd
import pymysql
from model.config import client


def puma_emo():
    comment = puma["comment"]
    product = puma["product"][0]
    product_id = puma["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def nike_emo():
    comment = nike["comment"]
    product = nike["product"][0]
    product_id = nike["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def adidas_emo():
    comment = adidas["comment"]
    product = adidas["product"][0]
    product_id = adidas["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def anta_emo():
    comment = anta["comment"]
    product = anta["product"][0]
    product_id = anta["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def peak_emo():
    comment = peak["comment"]
    product = peak["product"][0]
    product_id = peak["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def new_emo():
    comment = new["comment"]
    product = new["product"][0]
    product_id = new["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def asics_emo():
    comment = asics["comment"]
    product = asics["product"][0]
    product_id = asics["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def Ske_emo():
    comment = Skechers["comment"]
    product = Skechers["product"][0]
    product_id = Skechers["product_id"][0]
    for text in comment:
        time.sleep(0.4)
        result = client.sentimentClassify(text)
        try:
            for i in result["items"]:
                neg = i["negative_prob"]
                pos = i["positive_prob"]
                if 0.7 < neg < 1:
                    emotional = i["negative_prob"] = '负面'
                elif 0.7 < pos < 1:
                    emotional = i["positive_prob"] = '正面'
                else:
                    emotional = '中性'

                emo = {
                    'product': product,
                    'product_id': product_id,
                    'neg': neg,
                    'pos': pos,
                    'emotional': emotional,
                    'comment': text,
                }
                print(emo)
                write_db(product, product_id, neg, pos, emotional, text)
        except:
            print('=' * 30)


def write_db(product, product_id, neg, pos, emotional, text):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='jdspider')
    cursor = db.cursor()
    sql = """INSERT IGNORE INTO jdspider.emotional VALUES ('%s', '%s', '%s', '%s', '%s', '%s')
                """ % (product, product_id, neg, pos, emotional, text)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print('1' * 30)
        db.rollback()
    db.close()


if __name__ == '__main__':
    excutor = ThreadPoolExecutor(10)
    excutor.submit(write_db)
    puma_emo()
    peak_emo()
    new_emo()
    nike_emo()
    anta_emo()
    adidas_emo()
    asics_emo()
    Ske_emo()

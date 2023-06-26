import os
from collections import Counter
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import re
import jieba
from jieba import analyse
from sqlalchemy import create_engine
from wordcloud import WordCloud
from mysql import puma1, adidas1, anta1, asics1, peak1, Skechers1, new1, nike1
from model.config import stopword, engine


fir_coms1 = []
fir_coms2 = []
fir_coms3 = []
fir_coms4 = []
fir_coms5 = []
fir_coms6 = []
fir_coms7 = []
fir_coms8 = []
jieba.load_userdict('userdict.txt')  # 加载自定义词典


def get_comments():
    # 统计重复数据
    # r = reviews1[['comment', 'comment_type']].duplicated().sum()
    # 评论去重
    # reviews = reviews1[['comment', 'comment_type']].drop_duplicates()
    # 重置索引
    # reviews.reset_index(drop=True, inplace=True)
    # print(r)
    # 遍历每一条评论
    for line in adidas1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        # res.sub匹配
        # pattern : 正则中的模式字符串。
        # repl : 替换的字符串，也可为一个函数。
        # string : 要被查找替换的原始字符串。
        # count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
        # re.sub(pattern, repl, string, count=0, flags=0)
        fir_comment1 = re.sub(pattern, '', comment)
        fir_coms1.append(fir_comment1)
    for line in puma1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment2 = re.sub(pattern, '', comment)
        fir_coms2.append(fir_comment2)
    for line in new1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment3 = re.sub(pattern, '', comment)
        fir_coms3.append(fir_comment3)
    for line in anta1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment4 = re.sub(pattern, '', comment)
        fir_coms4.append(fir_comment4)
    for line in nike1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment5 = re.sub(pattern, '', comment)
        fir_coms5.append(fir_comment5)
    for line in peak1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment6 = re.sub(pattern, '', comment)
        fir_coms6.append(fir_comment6)
    for line in Skechers1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment7 = re.sub(pattern, '', comment)
        fir_coms7.append(fir_comment7)
    for line in asics1["comment"]:
        comment = line
        # 编译要去除的对象为数字英文
        pattern = re.compile('[a-zA-Z0-9]|：|')
        fir_comment8 = re.sub(pattern, '', comment)
        fir_coms8.append(fir_comment8)


def clean_word():
    key_words1 = []
    cloud_words1 = []
    key_words2 = []
    cloud_words2 = []
    key_words3 = []
    cloud_words3 = []
    key_words4 = []
    cloud_words4 = []
    key_words5 = []
    cloud_words5 = []
    key_words6 = []
    cloud_words6 = []
    key_words7 = []
    cloud_words7 = []
    key_words8 = []
    cloud_words8 = []
    front = "static/SanJiHuaXinJianTi-2.ttf"  # 字体路径
    image_background = Image.open("static/assets/img/adidas.jpg")  # 词云轮廓图 imread
    mask_image = np.array(image_background)

    wc = WordCloud(font_path=front,
                   background_color="white",
                   mask=mask_image)  # 词云图格式
    for fir_com1 in fir_coms1:  # 分词
        cut_list = jieba.cut(fir_com1, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                word += w
                word += ' '
        print(type(word))
        cut_list = jieba.cut(word)  # , cut_all=True
        print(cut_list)
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words1.append(tf_result)
        print(type(key_words1), key_words1)
    for item in key_words1:
        for i in item:
            cloud_words1.append(i)
    frequency1 = dict(Counter(cloud_words1))  # 删除停用词后的词频统计结果
    w1 = wc.fit_words(frequency1)
    plt.imshow(w1)  # 生成词云图
    plt.axis("off")
    plt.show()
    w1.to_file("wordcloud/阿迪达斯ADIDAS.jpg")  # 词云图保存路径
    for fir_com2 in fir_coms2:  # 分词
        cut_list = jieba.cut(fir_com2, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words2.append(tf_result)
    for item in key_words2:
        for i in item:
            cloud_words2.append(i)
    frequency2 = dict(Counter(cloud_words2))
    w2 = wc.fit_words(frequency2)
    plt.imshow(w2)
    plt.axis("off")
    plt.show()
    w2.to_file("wordcloud/彪马PUMA.jpg")
    for fir_com3 in fir_coms3:  # 分词
        cut_list = jieba.cut(fir_com3, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words3.append(tf_result)
    for item in key_words3:
        for i in item:
            cloud_words3.append(i)
    frequency3 = dict(Counter(cloud_words3))
    w3 = wc.fit_words(frequency3)
    plt.imshow(w3)
    plt.axis("off")
    plt.show()
    w3.to_file("wordcloud/NEWBALANCE.jpg")
    for fir_com4 in fir_coms4:  # 分词
        cut_list = jieba.cut(fir_com4, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words4.append(tf_result)
    for item in key_words4:
        for i in item:
            cloud_words4.append(i)
    frequency4 = dict(Counter(cloud_words4))
    w4 = wc.fit_words(frequency4)
    plt.imshow(w4)
    plt.axis("off")
    plt.show()
    w4.to_file("wordcloud/安踏ANTA.jpg")
    for fir_com5 in fir_coms5:  # 分词
        cut_list = jieba.cut(fir_com5, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words5.append(tf_result)
    for item in key_words5:
        for i in item:
            cloud_words5.append(i)
    frequency5 = dict(Counter(cloud_words5))
    w5 = wc.fit_words(frequency5)
    plt.imshow(w5)
    plt.axis("off")
    plt.show()
    w5.to_file("wordcloud/耐克NIKE.jpg")
    for fir_com6 in fir_coms6:  # 分词
        cut_list = jieba.cut(fir_com6, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words6.append(tf_result)
    for item in key_words6:
        for i in item:
            cloud_words6.append(i)
    frequency6 = dict(Counter(cloud_words6))
    w6 = wc.fit_words(frequency6)
    plt.imshow(w6)
    plt.axis("off")
    plt.show()
    w6.to_file("wordcloud/匹克PEAK.jpg")
    for fir_com7 in fir_coms7:  # 分词
        cut_list = jieba.cut(fir_com7, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words7.append(tf_result)
    for item in key_words7:
        for i in item:
            cloud_words7.append(i)
    frequency7 = dict(Counter(cloud_words7))
    w7 = wc.fit_words(frequency7)
    plt.imshow(w7)
    plt.axis("off")
    plt.show()
    w7.to_file("wordcloud/斯凯奇Skechers.jpg")
    for fir_com8 in fir_coms8:  # 分词
        cut_list = jieba.cut(fir_com8, cut_all=False)  # 分词结果
        word = ''
        for w in cut_list:  # 去停分词
            if w not in stopword:
                if word != '\t':
                    word += w
                    word += ' '
        cut_list = jieba.cut(word)  # , cut_all=True
        line = " ".join(cut_list)
        # TF-IDF提取关键词 topK 关键词数量
        tf_result = analyse.extract_tags(line, topK=10, )  # allowPOS=('n', 'nr', 'ns')
        key_words8.append(tf_result)
    for item in key_words8:
        for i in item:
            cloud_words8.append(i)
    frequency8 = dict(Counter(cloud_words8))
    w8 = wc.fit_words(frequency8)
    plt.imshow(w8)
    plt.axis("off")
    plt.show()
    w8.to_file("wordcloud/亚瑟士ASICS.jpg")


if __name__ == '__main__':
    get_comments()
    clean_word()

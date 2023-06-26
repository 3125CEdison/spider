import re
import pymysql
from aip import AipNlp
from sqlalchemy import create_engine


BASE_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId='
_score_url = '&score='
scoreType_url = '&sortType=6'
page_url = '&page='
other_url = '&pageSize=10&isShadowSku=0&fold=1'
url = "https://club.jd.com/comment/productPageComments.action"
headers = {
    "referer": "https://item.jd.com/",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 '
                  'Safari/537.36 ',
    "cookie": "JSESSIONID=3EF1E444413ADE8739DE9B58181EBCC8.s1; Path=/; HttpOnly"
}
url_inputs = {
    'https://item.jd.com/100018065813.html', 'https://item.jd.com/67309469981.html',  # 阿迪达斯 彪马
    'https://item.jd.com/100017977183.html', 'https://item.jd.com/100010012807.html',  # 斯凯奇 匹克
    'https://item.jd.com/100015163119.html', 'https://item.jd.com/10025818742036.html',  # 耐克 亚瑟士
    'https://item.jd.com/10034116992996.html', 'https://item.jd.com/10038719197887.html'  # 新百伦 安踏,
}
APP_ID = '30067462'
API_KEY = 'QiClUaCq95qFppiFmG24RSm8'
SECRET_KEY = 'LES0QjxS89YV5YE8StFOIf4HbrvBkZCY'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

# 停用词路径
stop_list = "usual.txt"
# 加载停用词表
stopwords = open(stop_list, 'r', encoding='utf-8')
# 遍历停用词表
stopword = [s.rstrip() for s in stopwords.readlines()]
print(stopword)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/jdspider', echo=True)

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='jdspider'
)
url_input = 'https://item.jd.com/10034116992996.html'  # input("请输入京东商品网址：")
id = ''.join(re.findall(r'com/(.*?)\.html', url_input))
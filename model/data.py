import pymysql


def gooddata():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_type) AS num FROM jdspider.jd_comment  WHERE comment_type = '好评'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    print(type(result))
    good_comment = []
    for item in result:
        good_comment.append(item)
    data1 = good_comment
    print(type(data1), dict(data1))
    cur.close()
    connect.close()
    return data1


def middledata():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_type) AS num FROM jdspider.jd_comment  WHERE comment_type = '中评'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    middle_comment = []
    for item in result:
        middle_comment.append(item)
    data2 = middle_comment
    print(data2)
    cur.close()
    connect.close()
    return data2


def baddata():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_type) AS num FROM jdspider.jd_comment  WHERE comment_type = '差评'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    bad_comment = []
    for item in result:
        bad_comment.append(item)
    data3 = bad_comment
    print(data3)
    cur.close()
    connect.close()
    return data3


def star5data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_level) AS num FROM jdspider.jd_comment  WHERE comment_level = '5'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    star5_comment = []
    for item in result:
        star5_comment.append(item)
    star5 = star5_comment
    print(star5)
    cur.close()
    connect.close()
    return star5


def star4data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_level) AS num FROM jdspider.jd_comment  WHERE comment_level = '4'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    star4_comment = []
    for item in result:
        star4_comment.append(item)
    star4 = star4_comment
    print(star4)
    cur.close()
    connect.close()
    return star4


def star3data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_level) AS num FROM jdspider.jd_comment  WHERE comment_level = '3'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    star3_comment = []
    for item in result:
        star3_comment.append(item)
    star3 = star3_comment
    print(star3)
    cur.close()
    connect.close()
    return star3


def star2data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_level) AS num FROM jdspider.jd_comment  WHERE comment_level = '2'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    star2_comment = []
    for item in result:
        star2_comment.append(item)
    star2 = star2_comment
    print(star2)
    cur.close()
    connect.close()
    return star2


def star1data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(comment_level) AS num FROM jdspider.jd_comment  WHERE comment_level = '1'" \
          "GROUP BY product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    star1_comment = []
    for item in result:
        star1_comment.append(item)
    star1 = star1_comment
    print(star1)
    cur.close()
    connect.close()
    return star1


def member1data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(member) AS num FROM jdspider.jd_comment  WHERE member = '普通会员'" \
          "GROUP BY member, product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    member1_comment = []
    for item in result:
        member1_comment.append(item)
    member1 = member1_comment
    print(member1)
    cur.close()
    connect.close()
    return member1


def member2data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(member) AS num FROM jdspider.jd_comment  WHERE member = 'plus会员'" \
          "GROUP BY member, product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    member2_comment = []
    for item in result:
        member2_comment.append(item)
    member2 = member2_comment
    print(member2)
    cur.close()
    connect.close()
    return member2


def emotion0data():
    data = []
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT * FROM jdspider.emotional"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        data.append(item)
    data = result
    # data = dict(result)
    print(data)
    cur.close()
    connect.close()
    return data


def emotion1data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(emotional) AS num FROM jdspider.emotional  WHERE emotional = '正面'" \
          "GROUP BY emotional, product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    emotion1_comment = []
    for item in result:
        emotion1_comment.append(item)
    emotion1 = emotion1_comment
    print(emotion1)
    cur.close()
    connect.close()
    return emotion1


def emotion2data():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT product,COUNT(emotional) AS num FROM jdspider.emotional  WHERE emotional = '负面'" \
          "GROUP BY emotional, product ORDER BY product"
    cur.execute(sql)
    result = cur.fetchall()
    print(type(result))
    emotion2_comment = []
    for item in result:
        emotion2_comment.append(item)
    emotion2 = emotion2_comment
    print(emotion2)
    cur.close()
    connect.close()
    return emotion2


def get_comment():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT * FROM jdspider.jd_comment ORDER BY creationTime DESC LIMIT 100 "
    cur.execute(sql)
    result = cur.fetchall()
    comment = []
    for item in result:
        comment.append(item)
    # comment = dict(comment)
    print(comment)
    cur.close()
    connect.close()
    return comment


def get_all():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT * FROM jdspider.sum"
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    all = []
    for item in result:
        all.append(item)
    # comment = dict(comment)
    print(all)
    cur.close()
    connect.close()
    return all


def sale1():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='67309469981'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale2():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00'AND product_id='100018065813'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale3():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='10034116992996'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale4():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='100017977183'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale5():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='10038719197887'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale6():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='100010012807'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale7():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='10025818742036'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


def sale8():
    connect = pymysql.connect(host="localhost", user="root", password="123456", db="jdspider")
    cur = connect.cursor()
    sql = "SELECT DATE_FORMAT(creationTime,'%Y%m') MONTH,COUNT(*) AS num FROM jdspider.jd_comment " \
          "WHERE creationTime BETWEEN '2023-01-01 00:00:00' AND '2023-05-30 00:00:00' AND product_id='10034116992996'" \
          "GROUP BY  MONTH "
    cur.execute(sql)
    result = cur.fetchall()
    time = []
    for item in result:
        time.append(item)
    comment = dict(time)
    print(comment)
    cur.close()
    connect.close()
    return comment


# gooddata()
# middledata()
# baddata()
# star1data()
# star2data()
# star3data()
# star4data()
# star5data()
# member1data()
# member2data()
# emotion0data()
# emotion1data()
# emotion2data()
# get_comment()
get_all()
# sale1()
# sale2()
# sale3()
# sale4()
# sale5()
# sale6()
# sale7()
# sale8()

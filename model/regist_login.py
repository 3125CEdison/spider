from model.config import connect

cur = connect.cursor()


def add_user(username, password):
    # sql commands
    sql = "INSERT INTO jdspider.users(username, password) VALUES ('%s','%s')" % (username, password)
    # execute(sql)
    cur.execute(sql)
    # commit
    connect.commit()  # 对数据库内容有改变，需要commit()

from model.config import connect

cur = connect.cursor()


def is_existed(username, password):
    sql = "SELECT * FROM jdspider.users WHERE username ='%s' and password ='%s'" % (username, password)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True


def exist_user(username):
    sql = "SELECT * FROM jdspider.users WHERE username ='%s'" % username
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True

from AI import puma_emo, peak_emo, new_emo, nike_emo, anta_emo, adidas_emo, asics_emo, Ske_emo
from WC import get_comments, clean_word
from badWC import get_bad, clean_bad
from goodWC import get_good, clean_good
from model.check_login import exist_user, is_existed
from model.regist_login import add_user
from model.data import gooddata, middledata, baddata, star1data, star2data, star3data, star4data, star5data, \
    member1data, member2data, emotion1data, emotion2data, emotion0data, get_comment, sale1, sale2, sale3, sale4, sale5, \
    sale6, sale7, sale8, get_all

from flask import Flask, render_template, request
from spider import write_db, crawler, get_sum, get_maxpage, parse, start_urls
from concurrent.futures import ThreadPoolExecutor
from threading import Event

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        if exist_user(username):
            login_massage = "温馨提示：用户已存在，请直接登录"
            # return redirect(url_for('user_login'))
            return render_template('login.html', message=login_massage)
        else:
            add_user(username, password)
            login_massage = "注册成功，请登录"
            return render_template('login.html', message=login_massage)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['name']
        password = request.form['password']
        if is_existed(username, password):
            return render_template('index.html')
        elif exist_user(username):
            login_massage = "温馨提示：密码错误，请输入正确密码"
            # return redirect(url_for('user_login'))
            return render_template('login.html', message=login_massage)
        else:
            login_massage = "温馨提示：不存在该用户，请先注册"
            return render_template('register.html', message=login_massage)


@app.route('/index', methods=["GET", "POST"])
def home():
    # return render_template("index.html")
    return render_template("index.html")


@app.route('/sum', methods=["GET", "POST"])
def sum():
    if request.method == "GET":
        tamp_data = get_all()
        return render_template("sum.html", map_data=tamp_data)


@app.route('/comment', methods=["GET", "POST"])
def comment():
    if request.method == "GET":
        tamp_data = get_comment()
        return render_template("comment.html", map_data=tamp_data)


@app.route('/updata', methods=["GET", "POST"])
def updata():
    if request.method == "GET":
        event = Event()
        excutor = ThreadPoolExecutor(10)
        excutor.submit(start_urls)
        excutor.submit(write_db)
        get_sum()
        get_maxpage()
        for i in range(2):
            excutor.submit(crawler, event)
        for i in range(6):
            excutor.submit(parse, event)
    return render_template("comment.html")


@app.route('/level', methods=["GET", "POST"])
def score():
    if request.method == "GET":
        tamp_data1 = dict(gooddata())
        tamp_data2 = dict(middledata())
        tamp_data3 = dict(baddata())
        tamp_data4 = gooddata()
        tamp_data5 = middledata()
        tamp_data6 = baddata()
        return render_template("level.html", map_data1=tamp_data1, map_data2=tamp_data2, map_data3=tamp_data3,
                               map_data4=tamp_data4, map_data5=tamp_data5, map_data6=tamp_data6)


@app.route('/star', methods=["GET", "POST"])
def star():
    if request.method == "GET":
        tamp_data5 = dict(star5data())
        tamp_data4 = dict(star4data())
        tamp_data3 = dict(star3data())
        tamp_data2 = dict(star2data())
        tamp_data1 = dict(star1data())
        tamp_data55 = star5data()
        tamp_data44 = star4data()
        tamp_data33 = star3data()
        tamp_data22 = star2data()
        tamp_data11 = star1data()
        return render_template("star.html", map_data1=tamp_data1, map_data2=tamp_data2, map_data3=tamp_data3,
                               map_data4=tamp_data4, map_data5=tamp_data5,
                               map_data11=tamp_data11, map_data22=tamp_data22, map_data33=tamp_data33,
                               map_data44=tamp_data44, map_data55=tamp_data55
                               )


@app.route('/member', methods=["GET", "POST"])
def member():
    if request.method == "GET":
        tamp_data1 = dict(member1data())
        tamp_data2 = dict(member2data())
        tamp_data3 = member1data()
        tamp_data4 = member2data()
        return render_template("member.html", map_data1=tamp_data1, map_data2=tamp_data2, map_data3=tamp_data3,
                               map_data4=tamp_data4)


@app.route('/sale', methods=["GET", "POST"])
def sale():
    if request.method == "GET":
        time_data1 = sale1()
        time_data2 = sale2()
        time_data3 = sale3()
        time_data4 = sale4()
        time_data5 = sale5()
        time_data6 = sale6()
        time_data7 = sale7()
        time_data8 = sale8()
        return render_template("sale.html", sale_data1=time_data1, sale_data2=time_data2, sale_data3=time_data3
                               , sale_data4=time_data4, sale_data5=time_data5, sale_data6=time_data6
                               , sale_data7=time_data7, sale_data8=time_data8)


@app.route('/emotional', methods=["GET", "POST"])
def emotional():
    if request.method == "GET":
        tamp_data1 = dict(emotion1data())
        tamp_data2 = dict(emotion2data())
        tamp_data3 = emotion1data()
        tamp_data4 = emotion2data()
        return render_template("emotional.html", map_data1=tamp_data1, map_data2=tamp_data2, map_data3=tamp_data3,
                               map_data4=tamp_data4)


@app.route('/emoupdata', methods=["GET", "POST"])
def emoupdata():
    if request.method == "GET":
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
    return render_template("emotional.html")


@app.route('/word', methods=["GET", "POST"])
def word():
    return render_template("word.html")


@app.route('/wordupdata', methods=["GET", "POST"])
def wordupdata():
    if request.method == "GET":
        get_comments()
        clean_word()
        get_bad()
        clean_bad()
        get_good()
        clean_good()
    return render_template("word.html")


@app.route('/nike', methods=["GET", "POST"])
def nike():
    return render_template("nike.html")


@app.route('/adidas', methods=["GET", "POST"])
def adidas():
    return render_template("adidas.html")


@app.route('/asics', methods=["GET", "POST"])
def asics():
    return render_template("asics.html")


@app.route('/ske', methods=["GET", "POST"])
def ske():
    return render_template("ske.html")


@app.route('/anta', methods=["GET", "POST"])
def anta():
    return render_template("anta.html")


@app.route('/peak', methods=["GET", "POST"])
def peak():
    return render_template("peak.html")


@app.route('/new', methods=["GET", "POST"])
def new():
    return render_template("new.html")


@app.route('/puma', methods=["GET", "POST"])
def puma():
    return render_template("puma.html")


if __name__ == '__main__':
    app.run()

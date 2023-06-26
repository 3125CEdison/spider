import re
from flask import Flask, render_template, request
from spider import write_db, crawler, get_sum, get_maxpage, parse, start_urls
from concurrent.futures import ThreadPoolExecutor
from threading import Event

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def qwe():
    return render_template("movie.html")


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
    return render_template("movie.html")


if __name__ == '__main__':
    app.run()

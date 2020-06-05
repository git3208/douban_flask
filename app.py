import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    return index()

@app.route('/movie')
def movie():
    datalist=[]
    conn=sqlite3.connect('movie.db')
    cur=conn.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('movie.html',datalist=datalist)

@app.route('/score')
def score():
    score=[]
    count=[]
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    # 我数据库不知道学哪去了，用这种方法
    # for i in range(80,100):
    #     sql = '''select rate from movie250 where rate=%f'''%(float(i/10))
    #     data = cur.execute(sql)
    #     temp=0
    #     for item in data:
    #         temp+=1
    #     if temp!=0:
    #         scores.append(float(i/10))
    #         count.append(temp)
    sql="select rate,count(rate) from movie250 group by rate"
    data=cur.execute(sql)
    for item in data:
        score.append(item[0])
        count.append(item[1])
    cur.close()
    conn.close()
    # 把两个列表合并成字典,实测好像不需要
    # datalist=dict(zip(scores,count))
    return render_template('score.html',score=score,count=count)

@app.route('/word')
def word():
    return render_template('word.html')

@app.route('/team')
def team():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()

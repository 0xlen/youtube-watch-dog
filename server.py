# -*- coding: utf-8 -*-
import os
import codecs
from GoogleTrend import GoogleTrend
from ngram import ngram
from salary import Salary
from flask import *
from werkzeug.utils import secure_filename

# Initialize application
app = Flask(__name__)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/salary/<username>')
def get_salary(username):
    user_salary = Salary(username)

    return user_salary.get()

@app.route('/comment')
@app.route('/comment/<video_id>')
def comment(video_id=''):

    comments = []
    comment_file = video_id + '.csv'
    if os.path.isfile(comment_file):

        file = codecs.open(comment_file, 'r', 'utf-8')
        for item in file:
            if len(item.split(',')) > 1:
                comments.append(item.split(',')[1])
        file.close()

        analytics = ngram()

        return render_template('comment.html', comments=comments, analytics=analytics.process(comments), max_count=analytics.getMax())
    else:
        return render_template('comment.html', comments=comments, analytics=[], max_count=0)

@app.route('/trend')
@app.route('/trend/<date>')
def trend(date=''):
    google_trend = GoogleTrend(geo = 'TW', hvd=date.replace('-', ''))
    trends = google_trend.get()

    # For debug
    # trends = []
    # with open('testfile', 'r') as f:
    #     for i in f:
    #         trends.append(i)

    analytics = ngram()

    return render_template('trend.html', trends=trends, date=date, analytics=analytics.process(trends), max_count=analytics.getMax())

# Start application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=None, debug=True)

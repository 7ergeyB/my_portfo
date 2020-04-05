# To launch the server run the following in the terminal down here:
# 1. ...>set FLASK_APP=web_server_main.py
#   Note: to activate the debug mode: set FLASK_ENV=development
# 2. ...>python -m flask run
#   Note: to make it publicly accessible, run: flask run --host=0.0.0.0
#   (where 0.0.0.0 is your machine IP - type 'ipconfig' in the cmd)

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def my_home():
    # return 'Всем привет от Сергея!'
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    # return 'Всем привет от Сергея!'
    return render_template(page_name)


# # Home:
# @app.route('/index.html')
# def home_again():
#     return render_template('index.html')


# # Works:
# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')
#
#
# # Work:
# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')
#
#
# # About:
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# # Contact:
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# # Components:
# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# app.run(host='0.0.0.0')
